f = open("file.txt","x")        #creating file, 2nd time error : FileExistsError: [Errno 17] File exists: 'file.txt'
f.write("hello\n")                #only allow write operation 
#f.read()                       #"io.UnsupportedOperation: not readable" due to opened file using "x" mode
f.write("hi\n")
#f.read()
f.close()
f = open("file.txt","r")
f.read()
f.write("enter your name")      #"io.UnsupportedOperation: not writable" error in r mode
f.read()