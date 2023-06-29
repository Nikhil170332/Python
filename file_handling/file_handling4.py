a = open("file.txt","w")
a.write("my name is nikhil, i am learning python")
#f.read()                       # error while reading, since it's mode is writable
print("file name is ", a.name)
print("file mode is ",a.mode)
print("file is readable? ",a.readable())
print("file is writeable? ",a.writable())
print("file is closed? ",a.closed)
a.close()
print("Now, file is closed? ",a.closed)

b = open("file.txt","r")
b.read()
b.close()


c = open("file.txt","w")
print("position of cursor ",c.tell())
c.write("Hi, how are you")                  # overwrite previous content
print("After writing position of cursor ",c.tell())     # position = 15
c.close()

d = open("file.txt","r+")
d.read()
d.seek(15)
d.write("\nI am adding text")       # along with reading using "r+" we can write content
print("After writing position of cursor ",d.tell())      # position = 32
d.close()

e = open("file.txt", "w+")
e.read()                            # since "w+/w" modes write operation, it overwrite previous content. so that data is deleted. so it is empty
e.write("File handling in python to operate with files in system")
e.read()                            # similar to "r+", "w+" can read and write the data
print("After writing position of cursor ",e.tell())         #position = 55
e.close()

f = open("file.txt","a")            # with "a" mode we create file and/or append data after the previous content
f.seek(0)
f.write("\nHi, how are you\nI am adding text")
#f.read()                                # unsupported read operation
f.close()


g = open("file.txt","a+")           # with "a+" mode we create file, read and/or append data after the previous content
g.read()
g.close