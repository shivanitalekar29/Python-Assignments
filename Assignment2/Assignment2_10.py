#WAP which accept no. from user and return addition of digits in that no.

def Sum():
    num = int(input("Enter the number:"))
    k=0
    while(num != 0):
        k=k+(num%10)
        num=num//10
    print(k)

def main():
    Sum()

if __name__ == "__main__":
    main()