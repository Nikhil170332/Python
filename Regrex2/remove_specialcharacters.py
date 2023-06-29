import re
date = input("enter anything (include special characters: ")
z = re.subn(r"[^a-zA-Z0-9]","",date)                         #subn returns 2 elements, 1st element is output string, 2nd element is count of replacements
print(f"modified date:{z[0]} \nNo of modifications: {z[1]}")