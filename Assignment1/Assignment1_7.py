#Write a program which contains one function that accept one number from user and returns true if number is divisible bye 5 otherwise return false.

def Chkdiv():
    num=int(input("Enter the number: "))
    if(num % 5 == 0):
        print(num,"is divisible by 5.")
    else:
        print(num,"is not divisible by 5.")

def main():
    Chkdiv()
    
if __name__ == "__main__":
    main()