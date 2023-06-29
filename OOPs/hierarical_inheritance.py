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
        
        
class Mobile1(Mobile):
    def additionaldetails(self,battery,display,camera):
        print("Additional Details")
        self.battery = battery
        self.display = display
        self.camera = camera
        print("Battery is {}\nDisplay is {}\nCamera  is {} ".format(self.battery,self.display,self.camera))
        print("---End---")
        
    
class Mobile2(Mobile):
    def additionaldetails(self,battery,display,camera):
        print("Additional Details")
        self.battery = battery
        self.display = display
        self.camera = camera
        print("Battery is {}\nDisplay is {}\nCamera  is {} ".format(self.battery,self.display,self.camera))
        print("---End---")
    
#Object creation
mobile1 = Mobile1("Iphone","Black")
mobile1.details("Iphone 13",125000)
mobile1.additionaldetails("4000mAH", "6-inch", "48MP+13MP")

mobile2 = Mobile2("Samsung","Green")
mobile2.details("Galaxy Note 20",100000)
mobile2.additionaldetails("6000mAH", "6.6-inch", "108MP+50MP+48MP")
