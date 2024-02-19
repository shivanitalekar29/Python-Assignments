import psutil

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            
            listprocess.append(pinfo);
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def Fileoutput():
    listprocess = ProcessDisplay()
    icnt = 0
    with open('Log1.txt', 'w') as log_file:
        for elem in listprocess:
            icnt+=1
            log_file.write(str(elem))
            log_file.write("\n")
        log_file.write(str(icnt))