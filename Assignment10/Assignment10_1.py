"""Design automation script which accept directory name and file extention from user. 
Display all files with that extension."""

from sys import *
import Assignment10_1module

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])
    try:
        if(len(argv) != 3):
            print("Invalid number of arguments")
            exit()

        else:
            Assignment10_1module.DirectoryTravel(argv[1],argv[2])
            
    except Exception as e:
        print("An error occurred:",e)

if __name__ == "__main__":
    main()
