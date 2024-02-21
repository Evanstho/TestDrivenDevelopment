def check_pwd(password):
    hasdigit = False
    hassymbol = False

    if not password:
        return False
    
    symbols = "~`!@#$%^&*()_+-="
    for char in password:
        if char.isdigit():
            hasdigit = True
        if char in symbols:
            hassymbol = True
    if not hasdigit or not hassymbol:
        return False

    return True