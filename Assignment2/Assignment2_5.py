#Check whether the number is prime or not.

def prime():
    num = int(input("Enter the number : "))
    k=0
    for i in range(2,num//2+1):
        if(num%i==0):
            k=k+1
    if(k<=0):
        print(num,"is prime number.")
    else:
        print(num,"is not a prime number.")

def main():
    prime()

if __name__ == "__main__":
    main()