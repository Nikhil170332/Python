number = int(input("Enter the number: "))
sum = 0
for i in range(1,number+1):
    sum = sum + i
    
print("the sum of first {} numbers is {}".format(number,sum))
print("the average of first {} numbers is {}".format(number,float(sum/number)))
