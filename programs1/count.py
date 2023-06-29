number = int(input("Enter the number: "))
rem = 0
digits = []
while number>0:
    rem = number%10
    digits.append(rem)
    number = number//10
print("Number of digits are {}".format(len(digits)))
