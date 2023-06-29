user = input("enter a word or name: ")
middle = int(len(user)/2)
new = user[middle-1]
new = new + (user[middle])
new = new + user[middle+1]
print(new)
