import os
from pathlib import Path
import shutil

def DirectoryTravel (DirName1, DirName2,name1):
    print("We are going to copy the files from",DirName1,"to new directory",DirName2,"with extension",name1)
    flag = os.path.isabs(DirName1)
    if not os.path.exists(DirName2):
        os.makedirs(DirName2)

    if flag == False:
        DirName = os.path.abspath(DirName1)

    exist = os.path.isdir(DirName1)


    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName1):
            print("Copied files in :")
            for fname in filename:
                if fname.endswith(name1):
                    src_file = os.path.join(DirName1, fname)
                    dest_file = os.path.join(DirName2, fname)
                    shutil.copy2(src_file,dest_file)
                    print(fname) 
                else:
                    print("File with the extension does not exits")
                    break
    else:
        print("Invalid path")