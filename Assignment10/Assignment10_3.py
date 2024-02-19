"""Design automation script which accept two directory names. Copy all files from first directory into second directory.
Second directory should be created at run time."""




"""import shutil
shutil.copytree('Hello1', 'foo')
shutil.copytree('baz', 'foo')"""

from sys import *
import Assignment10_3module

def main():
    print("----------Automation Script----------")
    print("Automation Script Name : ",argv[0])
    try:
        if(len(argv)!=3):
            print("Invalid number of arguments")
            exit()
        else:
            Assignment10_3module.copydirfile(argv[1],argv[2])

    except Exception as e:
        print("An error occurred:",e)

if __name__=="__main__":
    main()
