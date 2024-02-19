#WAP which contains one class named as Arithmetic. Arithemetic class contains three instance variable as Value1, Value2. Inside init method initialise all instance variable to 0. There are three instance methods inside class as Accept(), Addition(), Substraction, Multiplication(), Division(). Accept method will accept value1 and value2 from user. Addition() method will perform addtion of value1 and value2 and return result. subtraction()method will perform subtraction of value1, value2, and return result Division() method will perform multiplication of value1, value2 and return result. division() method will perfrom division of value1, value2 and return result.
#After designing the above class call all instanc methods by creating multiple objects

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        self.Result = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number:"))
        self.Value2 = int(input("Enter Second number:"))

    def Addition(self):
        self.Result = self.Value1 + self.Value2
        return print("Addition of",self.Value1,"and",self.Value2,"is",self.Result)
    
    def Substraction(self):
        self.Result = self.Value1 - self.Value2
        return print("Substraction of",self.Value1,"and",self.Value2,"is",self.Result)
    
    def Division(self):
        self.Result = self.Value1 / self.Value2
        return print("Division of",self.Value1,"and",self.Value2,"is",self.Result)
    
def main():
    obj = Arithmetic()
    obj.Accept()
    obj.Addition()
    obj.Substraction()
    obj.Division()

if __name__ == "__main__":
    main()