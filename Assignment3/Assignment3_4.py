#WAP which accept N numbers from user and store it into List. Accpt one another number from user and return frequncy of that number from list

def find_seq(list):
    num3 = int(input("Enter search element : "))
    b = 0
    for a in list:
        if a == num3:
            b = b + 1
    print(b)
    


def main():
    list1=[]
    num2 = 0
    num1 = int(input("Enter the number of elements : "))
    print("Enter elements : ")
    for i in range(0,num1):
        num2 = int(input())
        list1.append(num2)
    find_seq(list1)

      


if __name__ == "__main__":
    main()