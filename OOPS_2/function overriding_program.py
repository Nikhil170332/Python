#function overriding

class person:
    def __init__(self,fname,lname):
        print("constructor from Base class\n")
        self.first_name = fname
        self.last_name = lname 
    
    def display(self):
        print("Display method from base class")
        print("Full Name: ",(self.first_name+" "+self.last_name))
        
    def __del__(self):
        print("Destructor from base class")
        self.first_name = None
        self.last_name = None 

class student(person):
    
    def __init__(self,fname,lname,school):
        print("Constructor from derived class")
        person.__init__(self,fname,lname)
        self.school_name = school 
        
    def display(self):
        person.display(self)
        print("\nDisplay method from derived class")
        print("School name: ",self.school_name)
        
    def __del__(self):
        print("\nDestructor from Derived class") 
        person.__del__(self)
        self.school_name=None
        
object1 = student("Ravi","Teja","ZPH School")
object1.display()