#Mistakes in python "w+", "a+" and "r+" modes
'''
#1
file = open("New_file.txt","w+")    
file.read()                             #without using print(), you can't read
file.write("Hi\nHow are you\n")       
print(file.tell())                  
file.seek(5)
print(file.tell())
file.write(" anything want!\n")      
file.read()                             # since cursor position is at end of the characters of data in file, it won't print
file.close()

#2
f = open("New_file.txt","r+")
f.read()                                #without assigning it to a variable then not using print() of that variable, you can't read data
f.write("Now adding a new line\n"
f.read()                                #you read data wriiten, if you didn't change position of cursor at beginning
f.close()
'''
###########################################

#Tips to remember while reading data
#1 - always use print() to read() when you need to read data. (or) assign read method to a variable , then use taht variable in print() to read data.
#2 - Always reposition the cursor at beginning when you need to read full data in file

#correct way of reading

#1 
file = open("New_file.txt","w+")    
print(file.read())                      # first way - using print() to read content in file 
print("---------------")
file.write("Hi\nHow are you\n")       
print(file.tell()) 
file.seek(0)
data = file.read()                      # second way - assign read method to a variable called "data"
print(data)                             # use taht variable "data" in a print() to read content in file
print("---------------")
file.seek(15)
print(file.tell())
file.write("anything want!\n")
file.seek(0)                            # after rewriting, make sure when you want to read content reposition cursor at beginning 
print(file.read()) 
print("=====================")
file.close()


#2
f = open("New_file.txt","r+")
print(f.read())
print(f.tell())
f.seek(30)
f.write("\nNow writing data using 'r+' mode")           # writing something using "r+" mode
f.seek(0)                                               # repositing cursor at beginning
print(f.read())
print("----------------------")
print("now printing only newly added line only")
f.seek(30)                                              # repositing cursor at 30th character
print("-------------------------")
print(f.read())
f.close()
