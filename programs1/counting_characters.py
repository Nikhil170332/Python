user = input("enter a word or name: ")
characters =[]
for i in user:
    characters.append(i)
print(characters)
string1,number, synmbol = 0,0,0
for i in characters:
    if i.isalpha():
        string1 += 1
    elif i.isnumeric():
        number += 1
    else:
        synmbol += 1
print("string is {}, numbers is {}, synmbol is {}".format(string1,number,synmbol))
