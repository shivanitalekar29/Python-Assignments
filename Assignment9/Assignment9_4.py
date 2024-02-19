"""WAP which accept two file names from user and compare contents of both the files.
If both the files contains same contents then display success otherwise display failure.
Accpet names of both the files from command line."""

import sys
import os.path
def main():
    if len(sys.argv)!=3:
        sys.exit(1)
    Value1 = (sys.argv[1])
    Value2 = (sys.argv[2])
    if os.path.join(Value1,Value2):
        infile = open(Value1,"r")
        read_infile=infile.read()

        infile1 = open(Value2,"r")
        read_infile1=infile1.read()

        if read_infile==read_infile1:
            print("Content are same")
        else:
            print("Write")
    
if __name__=="__main__":
    main()