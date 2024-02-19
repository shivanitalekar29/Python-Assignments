#WAP which contains one lambda function which accepts one parameter and return power of two.

power = lambda No : 2 ** No
def main():
    num2 = 0
    print("Enter Number ")
    num = int(input())
    for i in range(num):
        num1 = power(i)
        num2 = num1 + 1 
    print(num2)


if __name__=="__main__":
    main()