user = input("enter a word or name: ")
length = len(user)
new = user[0]
new = new + (user[int(length/2)])
new = new + user[length-1]
print(new)
