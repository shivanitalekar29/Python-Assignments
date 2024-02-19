#Write a program which accept number from user and check whether the number is positove or negetive or zero.

def ChkNum():
    num = int(input("Enter the number: "))
    if(num>0):
        print(num,"is a positive number.")
    elif(num==0):
        print(num,"is Zero.")
    else:
        print(num,"is a negetive number.")

def main():
    ChkNum()

if __name__=="__main__":
    main()