with open("file.txt","a+") as f:
    n = int(input("Enter no of values to being added: "))
    ls = []
    for i in range(n):
        ls.append(input("Enter a value: "))
    f.writelines(f"The values are {ls}\n")
    f.seek(0)
    print(f.read())
    z =0
    for i in ls:
        z = int(i) + z
    f.write(f"The average of the values is {str(z/n)}")
    f.seek(0)
    print("-------------")
    print(f.read())
    print("===end===")