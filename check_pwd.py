def check_pwd(password):
    hasdigit = False
    hassymbol = False
    lower = False
    upper = False
    length = False

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
        if char.isupper():
            upper = True
    if not hasdigit or not hassymbol or not lower or not upper:
        return False

    if 8 <= len(password) <= 20:
        length = True
    if not length:
        return False

    return True