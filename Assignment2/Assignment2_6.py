# WAP which accept one no. and display below pattern.
# **
# *

def StarPattern():
    num = int(input("Enter the number:"))
    for i in range(0,num):
        for j in range(num,i,-1):
            print ("*",end=" ")
        print("\r")

def main():
    StarPattern()

if __name__ == "__main__":
    main()