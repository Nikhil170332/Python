number = int(input("Enter the range number: "))
order = []
rev_order = []
for i in range(1,number+1):
    order.append(input("Enter any value"))
for i in order[::-1]:
    rev_order.append(i)
print("the reverse order is",rev_order)
