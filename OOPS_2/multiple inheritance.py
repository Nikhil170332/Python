#multiple inheritance

class class1:
    def display(self):
        print("This is class1")
        
class class2(class1):
    def display(self):
        print("This is class2")
        super().display()
        
class class3(class1):
    def display(self):
        print("This is class3")
        super().display()
        
class class4(class2,class3):
    def display(self):
        print("This is class4")
        super().display()
        
cls = class4()
cls.display()
print(class4.mro())  
print(class4.__mro__)