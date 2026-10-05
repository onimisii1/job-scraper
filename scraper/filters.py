def is_match(title, include, exclude):
    check = title.lower()

    for word in exclude:          
        if word in check:         
            return False          

    for word in include:         
        if word in check:
            return True

    return False                  

print(is_match("Software Engineer", ["engineer"], ["manager"]))     # True
print(is_match("Engineering Manager", ["engineer"], ["manager"]))   # False