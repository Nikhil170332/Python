with open("file.txt","a+") as f:
    a = input("Enter a value:")
    b = input("Enter b value:")
    z = a+b 
    f.write(f"sum of {a} and {b} is {z}")
    f.seek(0)
    print(f.read())