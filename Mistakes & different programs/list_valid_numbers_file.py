import re 
with open("file.txt","a+") as f:
    n = int(input("Enter no of mobile numbers are adding: "))
    ls = []
    for i in range(n):
        ls.append(input("Enter a mobile number: "))
    f.write("Here the list of valid mobile numbers\n")
    z = 0
    for i in ls:
        p = re.compile("^[6-9]\d{9}$")
        if (re.search(p,i)):
            f.writelines(f"{i}\n")
        else:
            pass
    f.seek(0)
    print("-------------")
    print(f.read())
    print("===end===")
