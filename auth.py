def validate_password(password):
    # Check if password is not None and not empty
    if password is None:
        return False
    if len(password) == 0:
        raise ValueError("Password cannot be an empty string")
    return True

def login(user, password):
    if user is None or password is None:
        raise TypeError("Username and password cannot be None")
    try:
        if validate_password(password):
            return f"Welcome, {user}!"
    except ValueError as e:
        raise ValueError(str(e))
    return "Login failed"
