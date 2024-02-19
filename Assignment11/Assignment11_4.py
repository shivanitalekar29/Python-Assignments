import Assignment11_4module
from sys import *
import os
import time
import datetime

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

        starttime = time.time()
        arr = Assignment11_4module.DisplayChecksum(argv[1])
        endtime = time.time()
        print(starttime)
        print(endtime)

        print("The script took time to execute as : ",endtime-starttime)
        
  
    
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()