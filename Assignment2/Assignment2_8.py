#WAP which accept one number and display pattern
# 1 
# 1 2 
# 1 2 3

def numpatrn():
    num = int(input("Enter the number:"))
    for i in range(1,num+1):
        for j in range(1,i+1):
            print (j,end=" ")
        print(" ")

def main():
    numpatrn()

if __name__ == "__main__":
    main()