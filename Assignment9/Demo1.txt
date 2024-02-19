"""WAP which accept file name from user and create new file named as DEmo.txt amd copy all contemts from existing file into new file.Accept file name threogh commandline arguments"""

import sys
import os.path
def main():
    if len(sys.argv)!=2:
        sys.exit(1)
    Value1 = (sys.argv[1])
    if os.path.exists(Value1):
        infile = open(Value1,"r")
        read_infile=infile.read()
        fobj1 = open("Demo1.txt","w")
        fobj1.write(read_infile)
        print("Contents are copied from",Value1,"to",fobj1.name)
    
if __name__=="__main__":
    main()

