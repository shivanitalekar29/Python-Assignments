"""Design automation script which accecpt two directory names and one file extension. Copy all files with the specified extension from first directory into second directory.
Second directory should be created at run time."""

from sys import *
import Assignment10_4module

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])
    try:
        if(len(argv) != 4):
            print("Invalid number of arguments")
            exit()

        else:
            Assignment10_4module.DirectoryTravel(argv[1],argv[2],argv[3])
            
    except Exception as e:
        print("An error occurred:",e)

if __name__ == "__main__":
    main()
