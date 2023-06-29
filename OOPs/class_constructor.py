class Mobile:
    def __init__(self,brand,colour="black"):
        self.brand = brand          		#instance variables
        self.colour = colour				#instance variables
        
    def details(self,model,price):
        self.model = model
        self.price = price
        if self.brand == "Samsung":
            print("Brand is {} and colour {}".format(self.brand,self.colour))
            print("Model is {} and price is {}".format(self.model,self.price))
        else:
            print("Sorry!, only Samsung brand mobiles are available, please come again later")
    
#Object creation
mobile1 = Mobile("Samsung","white")
mobile1.details("Galaxy","1,18,000")
mobile2 = Mobile("Iphone")
mobile2.details("Iphone 13","78,000")

#object's memory locations
print(mobile1)          
print(mobile2)
