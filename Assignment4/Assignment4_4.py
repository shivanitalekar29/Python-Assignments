#WAP which contains filter(), map(), and reduce() in it. Python app which contains one list of numbers. List contaions the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map fumction will calculate its square. Reduce will return addition pf all that numbers.

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
    output = list(filter((lambda No: (No%2==0)),Data))
    print("Output after filter : ",output)

    moutput = list(map((lambda No:No*No),output))
    print("Output after map:",moutput)

    result = functools.reduce((lambda a,b:a+b),moutput)
    print(result)

if __name__ == "__main__":
    main();