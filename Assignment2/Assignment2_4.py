# WAP which accept one no. from user and return addtion of its factors

def factor():
    number = int(input("Enter the number:"))
    j=0
    for i in range(1,number+1):
        if(number%i==0):
            j=j+i
    print("Addition of factor",number,"is",j)

def main():
    factor()
            
if __name__ == "__main__":
    main()