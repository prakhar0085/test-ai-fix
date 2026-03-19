def validate_password(password):
    # Check if password is not None and not empty
    if password is None or len(password) == 0:
        return False
    return True

def login(username, password):
    if username is None or password is None:
        raise TypeError("Username and password cannot be None")
    if validate_password(password):
        return f"Welcome, {username}!"
    return "Login failed"
