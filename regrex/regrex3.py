import re
text="This is a python and it is easy to learn and there are 2 Pythons they are python_2/python2 and python_3/python3 3.5 3.72 65 @' ~ # % & * + - / ? and - are special characters "

pattern="\W"                    #find any character matches , but not part of \w 
print(re.findall(pattern,text))

pattern1 = "python[0-9]"        #matching python word with digits at end 
print(re.findall(pattern1,text))

pattern2 = "\d"                 # find any single digit match
print(re.findall(pattern2,text))

pattern3 = "\d\.\d"             # find float value using \d
print(re.findall(pattern3,text))

pattern4 = "\d\.\d\d"
print(re.findall(pattern4,text))