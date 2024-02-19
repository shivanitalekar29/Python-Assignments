import shutil
import os
def copydirfile(DirName1, DirName2):
    print("We are going to copy the Directory",DirName1,"files extention to",DirName2)
    flag = os.path.isabs(DirName1)

    if flag == False:
        DirName = os.path.abspath(DirName1)

    exist = os.path.isdir(DirName)

    if (exist == True):
        if (DirName2==False):
            shutil.copytree(DirName1, DirName2)
        else:
            print("Folder exists")
    else:
        print("Invalid path")

