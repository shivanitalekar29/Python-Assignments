#WAP which accept file name from user and open that file and display the contents of that file on screen.and

import os.path
def main():
    print("Enter the name of file that you want to create : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,'r')
        if fobj:
            print("File successfully opened in read mode")
            Data = fobj.read()
            print("Data from file",Data)
            fobj.close()
        else:
            print("Unable to open file")
    else:
        print("File does not exists")

if __name__=="__main__":
    main() 