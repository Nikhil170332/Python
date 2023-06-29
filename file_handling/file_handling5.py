f = open("file.txt","a+")
f.write("Hi my name is nikhil\n")
f.writelines(["This is writelines\n","where we use this method as to write list\n","Like this way\n","But It will add content as normally, not be in list\n"])
f.write("Just adding a new line\n")
f.close()

#read,readline and readlines method not working properly in "a+" mode

p = open("file.txt","r+")                     #so opening file as read mode "r+"
#read method

a1 = p.read()                                    # It will display all content in file
print(a1,)
a2 = p.read(8)                                   #display content upto 8 characters length
print(a2)
a3 = p.read(65)                                 #display content upto 65 characters length
print(a3)

#doubt below
"""
a4 = p.read()[4]                                #display content at 4th index character 
print(a4,"\n")
a5 = p.read()[5:40]                             #display content of range between 4 to 40
print(a5,"\n")
"""

#readline method 
b1 = p.readline()                               #first time readline , print 1st line
print(b1)
b2 = p.readline()                               #second time assigning returns 2nd line
print
b3 = p.readline()                               # similary every time assigning the readline to variable, we get next line as it go
while True:
    print(b3)
    b3 = p.readline()
    if not b3:
        break

#readlines method  
c1 = p.readlines()                              #returns with list of elements of each line
print(c1)
c2 = p.readlines()[2]                            # print 2nd line of the content, that means individual lines printed
print(c2)
c3 = p.readlines()[2:5]                         # print list index range between 2 to 5
print(c3)
p.close()