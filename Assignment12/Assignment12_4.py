"""Design automation script which accept directory name and mail id from user and create log file in that directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, Username. After creating log file send that log file to the specified mail"""
import sys
import Assigment12_4module

def main():
    print("Process Monitor")
    try:

        if(len(sys.argv)!=3):
            print("Invalid Number of arguments.")
            exit()
        else:
            result=Assigment12_4module.fileoutput(sys.argv[1])
            Assigment12_4module.email1(result,sys.argv[2])

    except Exception as e:
        print("An error occurred:",e)

 

if __name__=="__main__":

    main()

 

 