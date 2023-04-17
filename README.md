# netcut-and-reverce_shell
Controlling othe pc or phone with python
__________________________________
[#] install:
       ~$git clone https://github.com/omer-devil/netcut-and-reverce_shell/tree/main
       and move to the project directory:
             ~$cd netcut-and-reverce_shell
       now install the requirements
             ~$pip3 install -r requirements.txt
       
___________________________________
[#] how to use:
       first run Net-Cat on your computer:
               ~$python3 netcat.py
       then run reverce_shell on the target pc
               ~$python3 reverce_shell.py
       and then you get access to the target pc or phone
       note:-you can conver reverce_shell.py into .exe file or .apk file
            to conver it to .exe use pyinstaller and
            for .apk use buildozer
     
[#] all the command available with use and example:
    Commands.                 Use.                                  Example
    l-host.                   local-host <command>                  local-host ls
    download.                 download <file name>                  download music.mp4
    server.                   server <IP:PORT>                      server 127.0.0.1:468
    target-ip.                target-ip                             it shows the target ip
    output_save.              output_save <True/False>              output_seve True or output_save False
    
    help.                     shows this help message
