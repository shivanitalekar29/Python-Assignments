import os
from pathlib import Path

def DirectoryTravel (DirName, name1,name2):
    print("We are going to change the Directory",DirName,"file extention from",name1 , "to",name2)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                if fname.endswith(name1):
                    newfile = fname.replace(name1, name2)
                    os.rename(os.path.join(DirName, fname),os.path.join(DirName,newfile))
                    print(fname,":",newfile)
                else:
                    print("File with the extension does not exits")
                    break

    else:
        print("Invalid path")