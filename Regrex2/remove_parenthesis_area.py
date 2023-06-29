import re
def parenthesis(*args):
    lst = args
    for i in args:
        print(re.sub(r"\([^)]*\)","",i))
    
parenthesis("example (.com)", "w3resource", "github (.com)","stackoverflow (.com)")