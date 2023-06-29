class Mobile:
    def __init__(self,brand,colour="black"):
        self.brand = brand          #instance variables
        self.colour = colour
        
    def details(self,model,price):
        self.model = model
        self.price = price
        print("Brand: ",self.brand)
        print("colour: ",self.colour)
        print("model: ", self.model)
        print("price: ", self.price)
        
class NewMobile(Mobile):
    print("Here the details of Mobiles")
    
#Object creation
mobile1 = NewMobile("Iphone","Black")
mobile1.details("Iphone 13",125000)
