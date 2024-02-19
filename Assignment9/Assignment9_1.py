#WAP which accepts file name from user and check whether that file exists in currect directory or not

import os.path
def main():
    print("Enter the name of file that you want to create : ")
    File_name = input()
    if os.path.exists(File_name):
        print("File exists")
    else:
        print("File does not exists")
        #fobj = open(File_name,'x')

if __name__=="__main__":
    main()

