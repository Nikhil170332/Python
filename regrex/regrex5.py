import re
match=re.finditer("\s","a7Sb @k 9#Az")          #match with space
#match=re.finditer("\S","a7Sb @k 9#Az")         #match any character , except space
#match=re.finditer("\d","a7Sb @k 9#Az")         # any digit
#match=re.finditer("\D","a7Sb @k 9#Az")         # any character except digits
#match=re.finditer("\w","a7Sb @k 9#Az")         #any word character [a-zA-Z0-9]
#match=re.finditer("\W","a7Sb @k 9#Az")         #any character except word character
#match=re.finditer(".","a7Sb @k 9#Az")          # any character 
for m in match:
 print(m.start(),"......",m.group())            #m.group return matched pattern and m.start() gives index starting