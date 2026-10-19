import sys,os
SP=os.path.dirname(os.path.abspath(__file__))
L={"06":"c5-06-jobs","07":"c5-07-narrative-and-goals","08":"c5-08-captains-and-rivals","09":"c5-09-organizing-a-big-universe","10":"c5-10-a-boarding-site-on-the-map","11":"c5-11-a-ruin-on-the-map"}
help_=open(SP+"/help.py",encoding="utf-8").read()
for k in (sys.argv[1:] or L):
    p=SP+"/body%s.py"%k
    if not os.path.exists(p): continue
    s=open(p,encoding="utf-8").read().replace("#@HELP@",help_)
    open("E:/a/author_courses/%s/narration/storyboard.py"%L[k],"w",encoding="utf-8",newline="\n").write(s)
