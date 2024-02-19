"""Design automation script which accept process name and display information of that process if it is running. Usage : ProcInfo Notepad"""
import sys
import Assigment12_2module

def main():
    print("Process Monitor")
    try:

        if(len(sys.argv)!=2):
            print("Invalid Number of arguments.")
            exit()
        else:
            Assigment12_2module.fileoutput(sys.argv[1])

    except Exception as e:

        print("An error occurred:",e)

 

if __name__=="__main__":

    main()

 

 