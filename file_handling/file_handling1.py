file = open("New_file.txt","x")
file.close()
file = open("New_file.txt","a+")
file.write("Hi")
file.read()
file.close()