
def is_match(title, include, exclude):
    check = title.lower()

    for word in exclude:         
        if word in check:         
            return False          # one bad word is enough to reject
            
    for word in include:          
        if word in check:
            return True         # one good word is enough to accept

    return False                  # no good words found