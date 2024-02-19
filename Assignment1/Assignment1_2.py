# Write a program which contain one function names as ChkNum() which accepts one parameter as number. if number is even then it should display "Even number" otherwise display "Odd number" on console.
# input : 11    output : Odd Number

def ChkNum():
    num = 0
    num = int(input("Enter the number : "))
    if (num%2==0):
        print(num,"is even number.")
    else :
        print(num, "is odd number.")

def main():
    ChkNum()
 
if __name__ == "__main__":
    main()