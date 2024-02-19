#WAP which contains filter(), map(), and reduce(), in it. Python app whcih contains one list of numbers. Filter should filterout all prime numbers .Map fun will multipy each num by 2. Reduce will return max num from that num

import functools


def ChkPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def Max(x, y):
    if x < y:
        return y
    else:
        return x

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
    output = list(filter(ChkPrime,Data))
    print("Output after filter : ",output)

    moutput = list(map((lambda No:No*2),output))
    print("Output after map:",moutput)

    result = functools.reduce((Max),moutput)
    print("Output after reduce:",result)

if __name__ == "__main__":
    main();