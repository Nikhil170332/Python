def add(m):
    if alpha[m] == 1:
        return True

usr_string = input("Enter the string: ")
alpha = {}
characters = []
for i in usr_string:
    characters.append(i)
for j in characters:
    alpha[j]= characters.count(j)
    
x = "".join(list(filter(add,alpha.keys())))        
print(x)
