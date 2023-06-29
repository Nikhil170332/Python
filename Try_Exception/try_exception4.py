try:
    ls = [10,20,30]
    print("First element of lsit",ls[0])
    print("Second element of lsit",ls[1])
    #print(ls[5])               #Index error: index crosses the limit
    
    x = int(input("\nEnter a number:"))     #value error: Enter the number only
    y = int(input("Enter a number:"))
    #print(m)                   #Variable is not defind

    z = x/y 
    print("result", z)          #Denominator should not be zero
    
except IndexError:
    print("index error: index crosses the limit")
except NameError:
    print("Variable is not defind")
except ValueError as value:
    print("value error: Enter the number only")
except ZeroDivisionError:
    print("Denominator should not be zero")
finally:
    print("\nSession ended")
