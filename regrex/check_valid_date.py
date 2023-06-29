import re
date = input("enter the date in (YYYY-MM-DD):")
pattern = re.compile("(\d?)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])")
result = re.search(pattern,date)
if result != None:
    print("valid")
else:
    print("Not valid")