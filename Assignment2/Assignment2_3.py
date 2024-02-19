# WAP which accept one no. from user and return its factorials.

def fact():
    num = int(input("Enter the number: "))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)
def main():
    fact()


if __name__ == "__main__":
    main()