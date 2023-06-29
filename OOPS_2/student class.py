#student class

class Student:
    count = 0
    
    def __init__(self,number,name):
        self.number = number
        self.name = name
        Student.count= Student.count + 1
        print("Now the no of students is :",Student.count)
        
    def display(self):
        print("Student roll number",self.number)
        print("Student name", self.name)
        
    def __del__(self):
        Student.count = Student.count - 1
        print("After Removing student",self.name)
        print("Now no of students is ", Student.count)
        
    
print("No of Students: ",Student.count)

def number():
    rollno = int(input("Enter the Roll No: "))
    return rollno
def name():
    name = input("Enter the name: ")
    return name

student1 = Student(number(),name())
student2 = Student(number(),name())

student1.display()
student2.display()
student1 = None
student2 = None