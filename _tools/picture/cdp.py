"""Talk to a THROWAWAY VS Code window through the Chrome DevTools Protocol, to set up what a
still shows inside a webview (the Tile Map Editor's Art view, a legend row picked, the form
for a new entry, the cell under a pointer). Standard library only: a small WebSocket client.

The window is started with --remote-debugging-port (capture.py does it, for a still that asks
for "web" steps). Nothing here moves the real mouse or presses a real key: a step is a line of
JavaScript run in the webview's own page, or a synthetic mouse event sent to the window
through DevTools (for a hover that VS Code itself must see, such as a button's tooltip).

    import cdp
    page = cdp.webview(9333, "amd.tilesEditor")      # waits for the editor's frame
    page.run("document.querySelector('[data-mode=art]').click()")
"""
import base64
import json
import os
import socket
import struct
import time
import urllib.request


class Socket:
    """One WebSocket to one DevTools target."""

    def __init__(self, url, timeout=10):
        assert url.startswith("ws://")
        hostport, path = url[5:].split("/", 1)
        host, port = hostport.split(":")
        self.s = socket.create_connection((host, int(port)), timeout=timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
               f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n")
        self.s.sendall(req.encode())
        head = b""
        while b"\r\n\r\n" not in head:
            chunk = self.s.recv(4096)
            if not chunk:
                raise ConnectionError("DevTools closed the connection during the handshake")
            head += chunk
        head, self.buf = head.split(b"\r\n\r\n", 1)
        if b" 101 " not in head.split(b"\r\n")[0]:
            raise ConnectionError("DevTools refused the WebSocket: " + head.decode(errors="replace")[:200])
        self.next_id = 0
        self.events = []

    def _recv_exact(self, n):
        while len(self.buf) < n:
            chunk = self.s.recv(65536)
            if not chunk:
                raise ConnectionError("DevTools closed the connection")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def _frame(self):
        b1, b2 = self._recv_exact(2)
        n = b2 & 0x7F
        if n == 126:
            n = struct.unpack(">H", self._recv_exact(2))[0]
        elif n == 127:
            n = struct.unpack(">Q", self._recv_exact(8))[0]
        if b2 & 0x80:
            mask = self._recv_exact(4)
            data = bytes(x ^ mask[i % 4] for i, x in enumerate(self._recv_exact(n)))
        else:
            data = self._recv_exact(n)
        return b1 & 0x80, b1 & 0x0F, data

    def recv(self):
        parts, op = [], None
        while True:
            fin, opcode, data = self._frame()
            if opcode == 9:                                  # ping
                self._send(10, data)
                continue
            if opcode == 8:
                raise ConnectionError("DevTools closed the WebSocket")
            if opcode != 0:
                op = opcode
            parts.append(data)
            if fin:
                return json.loads(b"".join(parts).decode("utf-8")) if op == 1 else None

    def _send(self, opcode, data):
        mask = os.urandom(4)
        n = len(data)
        head = bytes([0x80 | opcode])
        if n < 126:
            head += bytes([0x80 | n])
        elif n < 65536:
            head += bytes([0x80 | 126]) + struct.pack(">H", n)
        else:
            head += bytes([0x80 | 127]) + struct.pack(">Q", n)
        self.s.sendall(head + mask + bytes(x ^ mask[i % 4] for i, x in enumerate(data)))

    def call(self, method, params=None, timeout=15):
        self.next_id += 1
        my = self.next_id
        self._send(1, json.dumps({"id": my, "method": method, "params": params or {}}).encode())
        t0 = time.time()
        while time.time() - t0 < timeout:
            msg = self.recv()
            if msg is None:
                continue
            if msg.get("id") == my:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})
            self.events.append(msg)
        raise TimeoutError(f"DevTools did not answer {method}")

    def close(self):
        try:
            self.s.close()
        except OSError:
            pass


def targets(port):
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=5) as r:
        return json.loads(r.read().decode("utf-8"))


class Webview:
    """The extension's own page inside a webview. VS Code puts it in an inner iframe
    (#active-frame); scripts are run in an isolated world of that frame, which shares its
    DOM and is not bound by the page's Content Security Policy (eval is)."""

    def __init__(self, sock, context):
        self.sock = sock
        self.context = context

    def run(self, js):
        """Evaluate JavaScript against the editor's page. -> its value (JSON-able), or raises."""
        res = self.sock.call("Runtime.evaluate", {"expression": js, "returnByValue": True, "awaitPromise": True,
                                                  "contextId": self.context})
        if res.get("exceptionDetails"):
            d = res["exceptionDetails"]
            raise RuntimeError(f"in the webview: {d.get('exception', {}).get('description') or d.get('text')}")
        return res.get("result", {}).get("value")


def _frames(tree):
    yield tree["frame"]
    for child in tree.get("childFrames", ()):
        yield from _frames(child)


def _editor_pages(sock):
    """Every webview's inner page this target holds, as a Webview."""
    sock.call("Page.enable")
    out = []
    for fr in _frames(sock.call("Page.getFrameTree")["frameTree"]):
        if fr.get("name") == "active-frame" and fr.get("url", "").startswith("vscode-webview://"):
            ctx = sock.call("Page.createIsolatedWorld", {"frameId": fr["id"], "worldName": "picture"})
            out.append(Webview(sock, ctx["executionContextId"]))
    return out


def webview(port, probe="!!document.getElementById('map')", timeout=40):
    """The webview whose page answers `probe` truthily, as soon as there is one."""
    t0 = time.time()
    last = None
    while time.time() - t0 < timeout:
        try:
            listing = targets(port)
        except OSError as e:
            last = e
            time.sleep(1)
            continue
        # A webview is an out-of-process frame, a target of its own; without site isolation
        # it would be a frame of the window's page. Look in both.
        for t in sorted(listing, key=lambda t: t.get("type") != "iframe"):
            if t.get("type") not in ("iframe", "page") or not t.get("webSocketDebuggerUrl"):
                continue
            sock = Socket(t["webSocketDebuggerUrl"])
            try:
                for page in _editor_pages(sock):
                    try:
                        if page.run(probe):
                            return page
                    except RuntimeError as e:
                        last = e
            except (RuntimeError, TimeoutError, ConnectionError) as e:
                last = e
            sock.close()
        time.sleep(1)
    raise RuntimeError(f"no webview answered {probe!r} on port {port} ({last or 'none found'})")


def window_page(port):
    """The VS Code window itself (the workbench), for an event VS Code must see."""
    for t in targets(port):
        if t.get("type") == "page" and t.get("webSocketDebuggerUrl") and t.get("url", "").startswith("vscode-file://"):
            return Socket(t["webSocketDebuggerUrl"])
    raise RuntimeError("no workbench page among the DevTools targets")
