import time 
try:
    x = int(input("enter a value "))
    y = int(input("enter a value "))
    z = x/y 
    print("wait for 5 seconds")
    time.sleep(5)
    
    print("result is ", z)
    
except ValueError:
    print("Enter integer values only")
except ZeroDivisionError :
    print("second value should not be zero")
except KeyboardInterrupt:
    print("Interrupt - cntrl C")