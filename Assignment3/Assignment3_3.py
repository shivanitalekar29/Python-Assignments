#WAP which accept N numbers from user and store it into List. Return Minimum number from that List

def find_min(list):
    min = list[0]
    for a in list:
        if a < min:
            max = a
    return max


def main():
    list1 = []

    num1 = int(input("Enter the number :"))
    print("Enter element : ")
    for i in range(0,num1):
        item = int(input())
        list1.append(item)
    print("Smallest number in the list is",find_min(list1))


if __name__ == "__main__":
    main()