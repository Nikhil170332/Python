#Encapsulation

class student:
    count = 0
    
    def __init__(self,rollno,name,age):
        self.__rollno = rollno
        self.__name = name
        self.__age = age
        student.count += 1
        self.__display()
        print("Now No of Students: {} \n".format(student.count))
        
    def __display(self):
        print("Roll No of Student:",self.__rollno)
        print("Name of the Student:",self.__name)
        print("Age of the Student:",self.__age)
        
    def __del__(self):
        student.count -= 1
        print(f"Student {self.__name} is deleted")
        print("After deleting, No of Students:", student.count)
    
object1 = student(1,"Sai",16)
#object1.__display()

object2 = student(2,"raj",14)
#object2.__display()

object1=None 
object2=None 