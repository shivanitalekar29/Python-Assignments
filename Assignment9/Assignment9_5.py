"""Accept file name and one string from user and return the frequency of that string from file"""

import sys
import os.path
def main():
    if len(sys.argv)!=3:
        sys.exit(1)
    Value1 = (sys.argv[1])
    Value2 = (sys.argv[2])
    if os.path.exists(Value1):
        infile = open(Value1,"r")
        read_infile=infile.read()

    frequency = read_infile.count(Value2)
    print(frequency)



    
if __name__=="__main__":
    main()