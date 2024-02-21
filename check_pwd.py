def check_pwd(password):
    hasdigit = False
    hassymbol = False
    lower = False

    if not password:
        return False
    
    symbols = "~`!@#$%^&*()_+-="
    for char in password:
        if char.isdigit():
            hasdigit = True
        if char in symbols:
            hassymbol = True
        if char.islower():
            lower = True
    if not hasdigit or not hassymbol or not lower:
        return False

    return True