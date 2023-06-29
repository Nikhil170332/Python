import re
text="This is pythonnnnn session and python is easy pythonn pythonnnn. It iis interpreted and it iiiis easy"

pattern=r'\bpython\b'
print(re.findall(pattern,text))

pattern1 = r'\bpython{1,5}\b'
print(re.findall(pattern1,text))

pattern2 = r'\bi{1,5}s\b'
print(re.findall(pattern2,text))