import re
def remove_low(string):
    text = string
    p = re.sub("[a-z]","",text)
    print(p)
    
remove_low(input("Enter a string: ")