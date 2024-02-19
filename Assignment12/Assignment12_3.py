"""Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username."""
import sys
import Assigment12_3module

def main():
    print("Process Monitor")
    try:

        if(len(sys.argv)!=2):
            print("Invalid Number of arguments.")
            exit()
        else:
            Assigment12_3module.fileoutput(sys.argv[1])

    except Exception as e:
        print("An error occurred:",e)

 

if __name__=="__main__":

    main()

 

 