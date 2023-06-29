n = int(input("Enter the no of lines:"))
cou = n
new = n
for i in range(1,n):
    for k in range(1,cou):
        print(end="  ")
    for j in range(i): 
        print("$", end="   ")
    cou = cou -1    
    print("\n")

for s in range(n,0,-1):
    for t in range(0,new-s):
        print(end="  ")
    for u in range(s):
        print("$",end= "   ")
    
    print("\n")
