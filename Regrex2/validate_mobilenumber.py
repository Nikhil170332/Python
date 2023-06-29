import re
number = input("Enter the number:")
p = re.compile("^\d{10}$")
if (re.search(p,number)):
    print("valid mobile number")
else:
    print("Not valid number")