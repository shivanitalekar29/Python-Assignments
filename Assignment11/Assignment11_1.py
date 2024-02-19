"""Design automation script which accept directory name and display checksum of all files
Useage : DirectoryChecksum.py "Demo" Demo is name of directory"""

import sys 
import Assignment11_1module
def main():
    print("--------Automation Script--------")
    print("Automation Script Name : ",sys.argv[0])

    try:
        if(len(sys.argv)!=2):
            print("Invalid Number of arguments.")
            exit()
        else:
            Assignment11_1module.FindCheckSUM(sys.argv[1])

    except Exception as e:
        print("An error occurred:",e)


if __name__=="__main__":
    main()

