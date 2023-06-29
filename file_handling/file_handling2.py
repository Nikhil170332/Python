file = open("New_file.txt","a+")    #file not exist create it, or append data
file.read()                         #read data, (comment 4th line to see result)
file.write("Hi\nHow are you")       #write data
file.read()
print(file.tell())                  #tell cusrsor position
file.seek(5)
print(file.tell())
#file.write(" anything want!")      #uncooment to see result of after modifying
file.read()
