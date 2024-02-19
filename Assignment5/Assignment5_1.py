#WAP which contains one class named as Demo. Demo class contains two instance variable no1, no2.
#that class contains one class variable as Value. There are two instance methods of class as FUN and GUN which displays values of instance variables. Initialise instance variable in init method by accepting the values from user.

class Demo:

    Value = 100

    def __init__(self,num1,num2):
        self.no1=num1
        self.no2=num2
    
    def FUN(self):
        print(self.no1)
        

    def GUN(self):
        print(self.no2)


def main():

    number1=int(input("Enter the number"))
    number2=int(input("Enter second number"))



    nem = Demo(number1,number2)
    nem.FUN()
    nem.GUN()
    print(nem.Value)

if __name__=="__main__":
    main()