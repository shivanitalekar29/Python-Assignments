#WAP which accept one no. and display below pattern
# 1 2
# 1 2

def noPattern():
    num = int(input("Enter the number:"))
    j = 1
    for i in range(1,num+1):
        for j in range(1,num+1):
            print (j,end=" ")
            j=j+i
        print("\r")

def main():
    noPattern()

if __name__ == "__main__":
    main()