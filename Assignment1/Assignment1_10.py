# Write a program which accept name from user and display length of its name.

def len():
    name=input("Enter the your name : ")
    y=0
    for i in name:
        y=y+1
    print("Length of your name is : ",y)

def main():
    len()

if __name__=="__main__":
    main()