def reverse(string):
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    return reverse_string
    
string = input("Enter a string: ")
result = reverse(string)
print("Original string {} , after reverse string {}".format(string,result))
