#WAP which contains one lambda fun which accepts two parameters and return its multiplication.

multi = lambda No1, No2 : No1 * No2
def main():
       
    print("Enter First Number:")
    num1 = int(input())
    print("Enter Second Number:")
    num2 = int(input())
    result=multi(num1,num2)
    print("Multiple of 2 numbers are : ",result)



if __name__=="__main__":
    main()