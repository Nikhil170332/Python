import os
class fruit:
    def __init__(self):
        print("Fruits: Mango , Apple , Grapes , Oranges")
        print("Choose the Fruit from above list")
        self.prices = {'Mango' : 70, 'Apple' : 110, 'Grapes' : 65, 'Oranges' : 80}
        self.items = {'Mango' : 30, 'Apple' : 25, 'Grapes' : 13, 'Oranges' : 20}
        self.money = []
        if not os.path.exists("sale.txt"):
            file = open("sale.txt","w+")
            file.write("List of items with prices\n----------------------------------------\n")
            for i in self.prices:
                file.write(f"{i} : price={self.prices[i]} and item amount={self.items[i]}\n")
            file.write("----------------------------------------\n")
            file.close()

class fruitSale(fruit):
    def sale(self,name,cost,kg):
        self.name_sale = cost
        self.kg = kg
        if self.items[name] > 0:
            self.cost = self.name_sale * self.kg
            print(f"The Total price of {name} is : {self.cost}₹")
            self.items[name] = self.items[name] - self.kg
            self.money.append(int(self.cost))
            return (f"=> Item purchased, {name} for {self.kg} : Total cost is {self.cost}\n")
        else:
            print(f"Sorry {name} item finished")
            return None
            
    def items_left(self):
        print(f"The items left  in kgs are {self.items}")
        print("Total money gain: ",sum(self.money),"₹")

class report():
    def __init__(self,note):
        file = open("sale.txt","a+")
        file.write(note)
        file.close()


try:  
    sales = fruitSale()
    fruit_name = input("Enter the fruit name:").title()
    amount = float(input(f"How many kgs of {fruit_name} you want:"))
    note = sales.sale(fruit_name,sales.prices[fruit_name],amount)
    if report!= None:
        obj = report(note)
    else:
        pass
    sales.items_left()
except KeyError:
    print("Please enter Fruit name correctly")
except ValueError:
    print("Please enter number only, not character ")

