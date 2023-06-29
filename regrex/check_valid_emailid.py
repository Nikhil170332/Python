import re
email = input("Enter a email address: ")
pattern = "^[a-z]([a-z0-9]+)\@[a-z]+\.([a-z]+)$"
p = re.compile(pattern)
if (re.search(pattern,email)):
    print("valid email")
else:
    print("Not a valid email")