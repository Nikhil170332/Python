#create a class with constructor and destructor

class Sample():
    def __init__(self,x,y):
        print("this is constructor")
        self.x =x
        self.y =y
        
    def add(self):
        print("The addition is", (self.x+self.y))
    def sub(self):
        print("The subtraction is", (self.x-self.y))
    def mul(self):
        print("The multiplication is", (self.x*self.y))
    def div(self):
        print("The division is", (self.x/self.y))
        
    def __del__(self):
        print("\nthis is destructor")
        
x = int(input("Enter a number"))
y = int(input("Enter a number"))
calculation1 = Sample(x,y)
calculation1.add()
calculation1 = None