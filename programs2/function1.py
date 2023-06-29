def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result1 = sum(20,43,56)
result2 = sum(45,23)
print(result1,"\n",result2)
