def is_match(title, include, exclude):
    check = title.lower()

    for word in exclude:          
        if word in check:         
            return False          

    for word in include:         
        if word in check:
            return True

    return False                  

