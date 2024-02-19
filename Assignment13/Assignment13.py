"""
Please follow below rules while designing automation script as
    1. Accept input through command line or through file
    2. Display any message in log file instead of console.
    3. For separate task define separate function.
    4. Perform validations before taking any action.
    5. Create user defined modules to store the fuctionality.
Design automation which performs following task.

Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.
Create one directory names of Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.
Name of that log file should contains the date and time at which that file removal after the specific time interval.
Accept Mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation of duplicate file removal.

Mail body should contains below things :
        Starting time of scanning
        Total number of files scanned
        Total number of duplicate files found

Consider below command line options for the gives script

DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

-DuplicateFileRemoval.py
    Name of python automation script

-E:/Data/Demo
    Absolute path of directory which may contains duplicate files

-marvellousinfosystem@gmail.com
    Mail ID of the receiver

Note:
For every separate task write separate function.
Write all user defined fuctions in one user defined module.
Use proper validation techniques.
Provide Help and usage option for script.
Create one Readme file which contains description of our script, details of command line options 
"""
import time
import schedule
import Assignment13_module
import sys
def main():
    print("Application name:"+sys.argv[0])
    if(len(sys.argv) == 2):
        if(sys.argv[1] =="-h" or sys.argv[1]=="-H"): 
            print("This automation script is used to remove duplicate file from a directory.")
            exit()
        elif(sys.argv[1] == "-u" or sys.argv[1]=="-U"):
            print("Usage: Name_Of_Script First_Argument Second_Argument third_argument")
            print("Example :Assignment13.py 1(timeinterval of script in minute) hello(folder name) example.gmail.com(email id)")
            exit()
        else:
            print("There is no such option to handle")
            exit()
    try:
        if(len(sys.argv)!=4):
                    print("Invalid Number of arguments.")
                    exit()
        else:
            schedule.every(int(sys.argv[1])).minutes.do(Assignment13_module.duplicate,sys.argv[2],sys.argv[3])
            while True:
                schedule.run_pending()
                time.sleep(1)

    except KeyboardInterrupt:
       print("Error:KeyboardInterrupt")
    except Exception as e:
       print("An error occurred:",e)


if __name__=="__main__":
    main()