#Write a program which accept N numbers from user and store it into List. Return addtion of all Elements from that List.

def CheckNum():
    num = int(input("Enter Number of elements : "))
    p = 0
    l = []
    print("Input Elements")
    for i in range(0, num):
        item = int(input())
        p = p + item
        l.append(item)
    print("Output : ",p)

def main():
    CheckNum()

if __name__ == "__main__":
    main()