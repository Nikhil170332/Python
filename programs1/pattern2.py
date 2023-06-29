number = int(input("Enter the number: "))
for i in range(1,number):
    for j in range(1,i):
        print("*",end= "  ")
    print("\n") 
for i in range(number,1,-1):
    for j in range(i,1,-1):
        print("*",end= "  ")
    print("\n") 
