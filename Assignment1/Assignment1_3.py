#Write a program which contain one function named as Add() which accepts two numbers from user and returns addtion of that two numbers.

def Add():
    print("Enter first number : ") 
    num1 = int(input())
    print("Enter second number : ")
    num2 = int(input())
    add = num1 + num2
    print("Addtion of above two numbers is ",add)

def main():
    Add()

if __name__ == "__main__":
    main()