

import psutil

def ProcessDisplay():
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

 

def fileoutput(var):
    listprocess = ProcessDisplay()
    with open('Log12.txt', 'w') as log_file:
       for elem in listprocess:
            if var == elem.get('name'):
                log_file.write(f"Process Name: {elem.get('name')}, PID: {elem.get('pid')}, Username: {elem.get('username')}\n")
     

               

       