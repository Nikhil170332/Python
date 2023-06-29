def count(items):
    counting = dict()
    for i in items:
        counting[i] = items.count(i)
    print(counting)
    
def main(number):
    items = []
    for i in range(number):
        items.append(input("Enter a number: "))
    print(items)
    count(items)
    
number = int(input("Enter the limit: "))
main(number) 
