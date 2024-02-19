#Create on module named as arithmetic which contains 4 functions for add for addition sub for subtraction, mult for multiplication and div for division. All funtions accpets parameters as number and perform the operation. Write on python program which call all the functions from arithmetic module by accepting the parameters from user.

import Arithmetic

def main(): 
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = Arithmetic.Add(a,b)
    print("Addition :",a,"+",b,"=",c)
    c = Arithmetic.Sub(a,b)
    print("Substraction :",a,"-",b,"=",c)
    c = Arithmetic.Mult(a,b)
    print("Multiplication :",a,"*",b,"=",c)
    c = Arithmetic.Div(a,b)
    print("Division :",a,"/",b,"=",c)

if __name__ == "__main__":
    main()
