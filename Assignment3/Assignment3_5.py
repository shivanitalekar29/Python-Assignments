#WAP which accept N num from user and store it into list. Return add of prime numbers from that list.
#MAin python file accept N numbers from user and pass each number to CHKPrime() fun which is part of our user defined module named as MarvellousNUM.
#Name of the function from main python file should be ListPrime()

import MarvellousNum

def ListPrime(numbers):
    prime_sum = 0
    for num in numbers:
        if MarvellousNum.ChkPrime(num):
            prime_sum += num
    return prime_sum

def main():
        n = int(input("Enter the number of elements: "))
        print("Enter elements:")
        num_list = []
        
        for i in range(n):
            num = int(input())
            num_list.append(num)
        
        result = ListPrime(num_list)
        print("Sum of prime numbers:", result)
    
if __name__ == "__main__":
    main()



