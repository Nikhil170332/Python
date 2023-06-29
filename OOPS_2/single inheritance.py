#single inheritance


class Details:
    
    def __init__(self):
        self.fname = input("Enter the first name: ")
        self.lname = input("Enter the last name: ")
        self.salary = int(input("Enter the salary: "))
        
    def display(self):
        print(f"Full name:{self.fname} {self.lname}\n")
    
class person(Details):
    
    def balance(self):
        self.spent = int(input("Enter the spent amount: "))
        if self.salary > self.spent:
            print("your balance is: ",(self.salary-self.spent))
        else:
            print("your balance is Lower than spent amount")
        

person1 = person()
person1.display()
person1.balance()
print("person class attributes",dir(person1))
print("perosn instant attributes",vars(person1))