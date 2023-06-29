my_str='''Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported'''
import re
#print(dir(re))
pat="i[stnc]"
print(f"Original String is '{my_str}'")
print(re.split(pat,my_str,flags=re.I))