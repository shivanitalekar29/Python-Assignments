from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    if exists:
        var = 0 #fdgsdf
        count = 0
        with open('Log.txt', 'w') as log_file:
            log_file.write("Duplicate Files:\n\n")
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                
                file_hash = hashfile(path) 
                if (file_hash == var):
                    count += 1
                    with open('Log.txt', 'a') as log_file:
                        log_file.write(f'Duplicate: {[file_hash]}\nDuplicate: {filen}\n\n')
                var = file_hash  
            if count == 0:
                    with open('Log.txt', 'w') as log_file:
                        log_file.write(f'No Duplicate files')

    else:
        print("Invalid Path")