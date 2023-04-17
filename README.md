# netcut-and-reverce_shell
Controlling othe pc or phone with python
__________________________________
[#] install:<br>
       ~$git clone https://github.com/omer-devil/netcut-and-reverce_shell/tree/main<br>
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
     
[#] all the command available with use and example:<br>
<p>    Commands.                 Use.                                  Example</p><br>
    l-host.                   local-host <command>                  local-host ls<br>
    download.                 download <file name>                  download music.mp4<br>
    server.                   server <IP:PORT>                      server 127.0.0.1:468<br>
    target-ip.                target-ip                             it shows the target ip<br>
    output_save.              output_save <True/False>              output_seve True or output_save False<br>
    <br>
    help.                     shows this help message<br>
