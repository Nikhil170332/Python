try:
    with open("Table.txt","+a") as f:
        n = int(input("Enter no of tables:"))
        for i in range(1,n+1):
            f.write(f"\n{i}'s Table\n-----------------\n")
            for j in range(1,11):
                f.write(f"{i} * {j} = {i*j}\n")
            f.write("------end-------")
except ValueError:
    print("Enter number only")