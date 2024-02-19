"""Design automation script which accept directory name and two file extensions from user. 
Rename all files with first file extension with the second file extension."""

from sys import *
import Assignment10_2module

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])
    try:
        if(len(argv) != 4):
            print("Invalid number of arguments")
            exit()

        else:
            Assignment10_2module.DirectoryTravel(argv[1],argv[2],argv[3])
            
    except Exception as e:
        print("An error occurred:",e)

if __name__ == "__main__":
    main()

