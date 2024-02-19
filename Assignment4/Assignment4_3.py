#WAP which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user.Filter should filter out all numbers. 
#List contains the numbers which are accepted from user.Filter should filter out all such numbers which greater that or equal to 70 and less than or equal to 90. Map function will increase easch number by 10. Reduce will return product of all that numbers.

import functools

def main():
    Data = [];
    print("Enter number of elements :")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    print("Input data : ",Data)
    print("Original list is:",Data)
    output = list(filter((lambda No: (No>=70 and No<=90)),Data))
    print("Output after filter : ",output)

    moutput = list(map((lambda No:No+10),output))
    print("Output after map:",moutput)

    result = functools.reduce((lambda a,b:a*b),moutput)
    print(result)

if __name__ == "__main__":
    main();