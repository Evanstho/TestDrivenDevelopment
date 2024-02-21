def check_pwd(password):
    hasdigit = False

    if not password:
        return False
    
    for char in password:
        if char.isdigit():
            hasdigit = True
    if not hasdigit:
        return False

    return True