#WAP which contains one class named as Circle. Circle class contains three instance variables as Radius, Area, Circumference. That class contains one class variable as P1 which is initialise to 3.14
#Inside init method initialise all instance variables to 0.0 There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display. Accept method will accept value of Radius from user.
#CalculateArea() method will calculate are of circle and store it into instance variable Area. CalculateCircumference() method will calculate circumference of circle and store it into instance variable circumference. After designing the above class call all instance methods by creating multiple objects

class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the value of radius : "))

    def CalculateArea(self):
        self.Area = self.PI * (self.Radius**2)

    def CalculateCircumference(self):
        self.Circumference = 2*self.PI * self.Radius

    def Display(self):
        print("Radius",self.Radius)
        print("Area",self.Area)
        print("Circumference",self.Circumference)

    
def main():

    cir = Circle()
    cir.Accept()
    cir.CalculateArea()
    cir.CalculateCircumference()
    cir.Display()

    cir1 = Circle()
    cir1.Accept()
    cir1.CalculateArea()
    cir1.CalculateCircumference()
    cir1.Display()   


if __name__=="__main__":
    main()