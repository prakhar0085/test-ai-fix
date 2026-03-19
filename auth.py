def validate_password(password):
    # BUG: special characters like @#$ break this check
    if password.isalnum():
        return True
    return False

def login(username, password):
    if validate_password(password):
        return f"Welcome, {username}!"
    return "Login failed"
