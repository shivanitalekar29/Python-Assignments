#Write a program which display first 10 even numbers on screen

def ChkEven():
    num = 1
    print("First 10 even numbers are:")
    while(num<=10):
        if(num%2==0):
            print(num, end = ' ')
        num=num+1

def main():
    ChkEven()

if __name__ == "__main__":
    main()