import os
import requests

f = os.popen("df -H")
res = f.read().split("\n")
da = None
for r in res:
    if "/dev/vda1" in r:
        arr = r.split(" ")
        da = [i for i in arr if i]
title = "磁盘空间使用情况"
msg = f"已用{da[2]}，可用{da[3]}，已用占比{da[4]}，总空间{da[1]}".replace(".", "\.").replace(
    "%", "\%"
)
r = requests.post(f"https://ali_bot.weqopy.workers.dev/?title={title}&msg={msg}")
