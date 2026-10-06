# Look at, and click in, the real engine's windows.
#
#   eng.ps1 -Action list
#   eng.ps1 -Action shot  -ProcId 1234 -Name airlock
#   eng.ps1 -Action click -ProcId 1234 -FracX 0.5 -FracY 0.9 [-Name after]
#
# DPI-aware first, and every coordinate comes from the window's CLIENT rect: without both,
# clicks land about 25% off. A click is refused unless the target window really is in front.
param(
    [string]$Action = "list",
    [int]$ProcId = 0,
    [string]$Name = "shot",
    [double]$FracX = 0.5,
    [double]$FracY = 0.5,
    [string]$OutDir = "$PSScriptRoot\shots",
    [int]$Settle = 1500
)

Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
public struct RECT { public int Left, Top, Right, Bottom; }
public struct POINT { public int X, Y; }
public static class W {
    [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
    [DllImport("user32.dll")] public static extern bool GetClientRect(IntPtr h, out RECT r);
    [DllImport("user32.dll")] public static extern bool ClientToScreen(IntPtr h, ref POINT p);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
    [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int cmd);
    [DllImport("user32.dll")] public static extern bool BringWindowToTop(IntPtr h);
    [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr after, int x, int y, int cx, int cy, uint flags);
    [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
    [DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, uint d, UIntPtr e);
    [DllImport("user32.dll")] public static extern void keybd_event(byte vk, byte scan, uint flags, UIntPtr e);
}
"@
[void][W]::SetProcessDPIAware()

function Get-Engines {
    Get-CimInstance Win32_Process -Filter "Name like 'Artemis3%'" | ForEach-Object {
        $p = Get-Process -Id $_.ProcessId -ErrorAction SilentlyContinue
        $kind = "client"
        if ($_.CommandLine -match "autostartserver") { $kind = "server" }
        [pscustomobject]@{ Id = $_.ProcessId; Kind = $kind; Handle = $p.MainWindowHandle; Title = $p.MainWindowTitle }
    }
}

function Get-Client([IntPtr]$h) {
    $r = New-Object RECT
    [void][W]::GetClientRect($h, [ref]$r)
    $o = New-Object POINT
    [void][W]::ClientToScreen($h, [ref]$o)
    [pscustomobject]@{ X = $o.X; Y = $o.Y; W = $r.Right - $r.Left; H = $r.Bottom - $r.Top }
}

function Front([IntPtr]$h) {
    # ALT tap first: Windows refuses SetForegroundWindow from a background process
    # unless it has just seen input.
    [W]::keybd_event(0x12, 0, 0, [UIntPtr]::Zero)
    [W]::keybd_event(0x12, 0, 2, [UIntPtr]::Zero)
    [void][W]::ShowWindow($h, 9)
    # Top-left of the screen, size unchanged: a window hanging off the right edge
    # captures as a white band and cannot be clicked there.
    [void][W]::SetWindowPos($h, [IntPtr]::Zero, 0, 0, 0, 0, 0x0001 -bor 0x0004)
    [void][W]::BringWindowToTop($h)
    [void][W]::SetForegroundWindow($h)
    Start-Sleep -Milliseconds 400
    return ([W]::GetForegroundWindow() -eq $h)
}

function Shot([IntPtr]$h, [string]$name) {
    $c = Get-Client $h
    if ($c.W -le 0 -or $c.H -le 0) { "window has no client area"; return }
    New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
    $bmp = New-Object System.Drawing.Bitmap $c.W, $c.H
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.CopyFromScreen($c.X, $c.Y, 0, 0, (New-Object System.Drawing.Size $c.W, $c.H))
    $path = Join-Path $OutDir ($name + ".png")
    $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose()
    "saved $path ($($c.W)x$($c.H))"
}

if ($Action -eq "list") { Get-Engines | Format-Table -AutoSize; return }

$proc = Get-Process -Id $ProcId -ErrorAction Stop
$h = $proc.MainWindowHandle
if ($h -eq [IntPtr]::Zero) { "process $ProcId has no window"; return }
$front = Front $h
if (-not $front) { "REFUSED: window of $ProcId is not in front (someone else has focus)"; return }

if ($Action -eq "shot") { Shot $h $Name; return }

if ($Action -eq "click") {
    $c = Get-Client $h
    $x = [int]($c.X + $c.W * $FracX)
    $y = [int]($c.Y + $c.H * $FracY)
    [void][W]::SetCursorPos($x, $y)
    Start-Sleep -Milliseconds 150
    [W]::mouse_event(2, 0, 0, 0, [UIntPtr]::Zero)
    Start-Sleep -Milliseconds 80
    [W]::mouse_event(4, 0, 0, 0, [UIntPtr]::Zero)
    "clicked $ProcId at ($FracX, $FracY) = screen ($x, $y)"
    Start-Sleep -Milliseconds $Settle
    Shot $h $Name
}
