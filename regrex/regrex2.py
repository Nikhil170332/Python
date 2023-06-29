import re
text="Python is easy-to-learn yet powerful and versatile scripting-language, Python's syntax and dynamic typing with its interpreted."
pattern="i[stn]"
print(re.findall(pattern,text)) 
print(len(re.findall(pattern,text)))

pattern1 = "[a-k A-Z]"
print(re.findall(pattern1,text))
print("\n")

pattern2="\w"                       #any alphabet character, digit or _ but no spcaes
print(re.findall(pattern2,text))
print("\n")

pattern3 = "\w\w\w"                 #any 3 string with 3 character length
print(re.findall(pattern3,text))
print("\n")