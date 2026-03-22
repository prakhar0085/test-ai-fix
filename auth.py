import hashlib

def validate_password(password):
    # Check if password is not None and not empty
    if password is None:
        return False
    if len(password) == 0:
        raise ValueError("Password cannot be an empty string")
    return True

def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password, stored_password):
    if username is None or password is None:
        raise TypeError("Username and password cannot be None")
    try:
        if validate_password(password):
            # Hash the input password and compare it to the stored password
            if hash_password(password) == stored_password:
                return f"Welcome, {username}!"
    except ValueError as e:
        raise ValueError(str(e))
    return "Login failed"

# Example usage:
stored_password = hash_password("secret@123")
print(login("john", "secret@123", stored_password))  # Output: Welcome, john!
print(login("john", "wrongpassword", stored_password))  # Output: Login failed
