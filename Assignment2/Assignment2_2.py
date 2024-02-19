# WAP which accept one no. from user and display below stars
# * * *
# * * *
# * * *

def star():
    num = int(input("Enter the number : "))

    for i in range(num):
        for j in range(num):
            print ("*",end=" ")
            j = j+1
        print("\r")


def main():
    star()

if __name__ == "__main__":
    main()