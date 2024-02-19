"""Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt file should be created into current directory. DirectoryDusplicate.py "Demo" """


import Assignment11_2module
from sys import *


def main():

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = Assignment11_2module.DisplayChecksum(argv[1])
        
  
    
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()