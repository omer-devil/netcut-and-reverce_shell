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
