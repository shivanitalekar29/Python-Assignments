import psutil
import os
from pathlib import Path

def ProcessDisplay():
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

def fileoutput(directory_name):
    listprocess = ProcessDisplay()
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    file_name = "Log221.txt"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as output_file:
        for elem in listprocess:
                output_file.write(str(elem))


               

       