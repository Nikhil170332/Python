import re
text = ['hello', 'hi', 'bye']
pattern = input("Which string you want:")
for i in text:
    z = re.match(pattern,i)
    if z!=None:
        print(z.group(),":Match found")
    else:
        print(i,":match not found")