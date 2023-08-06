import subprocess
import os
import time
import json
import requests
import platform
import sys
import shutil
from threading import Thread

def downloadFile(fpath):
    print('Downloading Ohmm Driver')
    url="https://ohmm.s3.amazonaws.com/ohmm-driver.exe"

    local_filename = fpath
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

def checkExists(fpath):
    ostype=platform.system()
    if("Windows" in ostype):
        fpath=fpath+"ohmm-driver.exe"
    elif('Linux' in ostype):
        fpath=fpath+"ohmm-driver"

    check=os.path.exists(fpath)
    #print(check)
    if(not check):
        downloadFile(fpath)

def get_chrome_version():
    process = subprocess.Popen(
        ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
    )
    version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
    version=version.split(".")[0]
    return version
def installdatakund():
    version=get_chrome_version()
    url="http://127.0.0.1:5000/install"
    headers = {'Content-type': 'application/json'}
    api_data={"userid":"","browser":"chrome","majorVersion":version,"tech_type":"PIP"}
    
    res=requests.post(url = url, data = json.dumps(api_data), headers=headers)
    res=json.loads(res.text)
def start_exe(exe_path):
    os.startfile(exe_path)
def startdatakund(folderpath):
    try:
        installdatakund()
        return 0
    except Exception as e:
        folderpath="C:/Users/datak/Desktop/ohmm-pip/ohmm/"
        checkExists(folderpath)
        dirpath=folderpath+"ohmm-driver.exe"
        #print(dirpath)
        print("Starting Ohmm Driver...")
        try:
            os.startfile(dirpath)
        except Exception as e:
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = ""
            exe_path = os.path.join(base_path, 'DataKund.exe')
            Thread(target = start_exe,args=(exe_path,)).start()
    i=0
    while(i<120):
        try:
            installdatakund()
            break
        except:
            time.sleep(1)
        i=i+1
def checkifinstall(folderpath):
    ostype=platform.system()
    if("Windows" in ostype):
        startdatakund(folderpath)
        serverurl="http://127.0.0.1:5000/"
    else:
        serverurl=" "
    return serverurl