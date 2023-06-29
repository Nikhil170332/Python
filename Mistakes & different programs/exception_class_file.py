class calculation(Exception):
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
        
    def add(self):
        return (self.a + self.b) 
        
    def sub(self):
        return (self.a - self.b)
    
    def mul(self):
        return (self.a * self.b)
        
    def div(self):
        return (self.a/self.b)

a = input("Enter a value:")
b = input("Enter b value:")
cal = calculation(a,b)
try:
    f = open("file.txt","a+")
    f.write(f" addition of {a} and {b} is {str(cal.add())}\n")
    f.write(f" subtraction of {a} and {b} is {str(cal.sub())}\n")
    f.write(f" multiplication of {a} and {b} is {str(cal.mul())}\n")
    f.write(f" division of {a} and {b} is {str(cal.div())}\n")
    f.seek(0)
    z = f.readlines()
    for i in z:
        print(i)
except ZeroDivisionError:
    print("second value 'b' should not be zero for division")
    f.write("Second value is zero, so division operation is aborted")
finally:
    f.close()