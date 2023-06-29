#multi level inheritance

class country:
    def __init__(self):
        print("Country : India")
    def classname(self):
        print("Country is in class1")

class state(country):
    def __init__(self):
        print("State : Andhra Pradesh")
        super().__init__()
    def classname(self):
        print("State is in class2")
        super().classname()
        
class district(state):
    def __init__(self):
        print("District : Anantapur")
        super().__init__()
    def classname(self):
        print("\nDistrict is in class3")
        super().classname()
        
location1 = district()
location1.classname()
print(district.mro())
print(district.__mro__)