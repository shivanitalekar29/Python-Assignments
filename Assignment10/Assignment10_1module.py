import os
def DirectoryTravel (DirName, name):
    print("We are going to change the Directory",DirName,"file extention",name)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                if fname.endswith(name):
                    print(fname)
                else:
                    print("File does not exist")
                    return
    else:
        print("Invalid path")

