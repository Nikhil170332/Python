try:
    print("File Open")
    a = 5
    b = 0
    print(a/b)
except Exception:
    print("Denomainator should not be zero")
    
finally:
    print("File close")