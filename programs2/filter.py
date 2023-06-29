def even(number):
    if number%2 == 0:
        return number
lst = [12,23,34,45,56,67,43]
result = list(filter(even,lst))
print(result)
