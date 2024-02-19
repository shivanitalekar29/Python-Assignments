#WAP which accepts N number from user and store it into List. Return Maxmimum number from that list.

def find_max(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max

def main():
    list1 = []

    num1 = int(input("Enter the number:"))
    print("Enter element : ")
    for i in range(0,num1):
        item = int(input())
        list1.append(item)
    print("Largest number in the list is",find_max(list1))
   

if __name__ == "__main__":
    main()