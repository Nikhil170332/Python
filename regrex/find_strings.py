import re
text = 'The quick brown fox jumps over the lazy dog.'
patterns = ['fox', 'dog', 'jump']
for i in patterns:
    match = re.search(i,text)
    if match !=None:
        print(f"{i} in found in {text} at {match.start()}")
    else:
        print("match not found")