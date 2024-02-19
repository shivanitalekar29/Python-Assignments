#WAP which accept no. from user and return number of digits in that no.

def NumDig():
    num = int(input("Enter the number:"))
    count = 0
    num1=1
    while(num>0):
        count=count+1
        num=num//10
        #num=num+1
    print("The number of digit is",count)


def main():
    NumDig()

if __name__ == "__main__":
    main()