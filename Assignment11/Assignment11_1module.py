import hashlib
import os

def md5(file1):
    md5h = hashlib.md5()
    with open(file1, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5h.update(chunk)
    return md5h.hexdigest()

def FindCheckSUM(path):
    flag = os.path.isabs(path)

    if flag == False:
        os.path.abspath(path)
    
    exists = os.path.isdir(path)

    if exists:
        for dirname, subdir, file in os.walk(path):
            print("Current folder name is : ",dirname)
            for fname in file:
                path = os.path.join(dirname,fname)
                hashfile = md5(path)
                print(path)
                print(hashfile)
                print(' ')
    else:
        print("Invalid Path")




