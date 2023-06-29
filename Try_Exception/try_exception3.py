def dictionary(key):
    try:
        data = {"madurai": "1103KM", "banglore":"500KM", "hyderabad":"700KM", "pune":"1200KM"}
        print(data[key])
        #print(data["vizag"])           #check your key or choose other key, it is not present
    except KeyError:
        print("check your key or choose other key, it is not present")
        print("available places are", list(data.keys()))
        
    finally:
        print("session closed")
    
dictionary(input("Enter a place "))