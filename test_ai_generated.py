import pytest
from auth import login, validate_password

def test_login_valid_credentials():
    """
    Test the login function with valid credentials.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"

def test_login_none_username():
    """
    Test the login function with None username.
    """
    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)

def test_login_none_password():
    """
    Test the login function with None password.
    """
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)

def test_login_empty_password():
    """
    Test the login function with empty password.
    """
    user = "test_user"
    password = ""
    with pytest.raises(ValueError):
        login(user, password)

def test_login_long_password():
    """
    Test the login function with a long password.
    """
    user = "test_user"
    password = "a" * 1000
    assert login(user, password) == f"Welcome, {user}!"

def test_login_password_with_special_chars():
    """
    Test the login function with a password containing special characters.
    """
    user = "test_user"
    password = "test_password!@#$"
    assert login(user, password) == f"Welcome, {user}!"

def test_validate_password_none():
    """
    Test the validate_password function with None password.
    """
    password = None
    assert not validate_password(password)

def test_validate_password_empty():
    """
    Test the validate_password function with empty password.
    """
    password = ""
    with pytest.raises(ValueError):
        validate_password(password)

def test_validate_password_valid():
    """
    Test the validate_password function with a valid password.
    """
    password = "test_password"
    assert validate_password(password)

def test_login_fix_specific_bug():
    """
    Test the specific bug fix by checking if the login function raises a TypeError when called with None username or password.
    """
    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)

def test_login_fix_edge_cases():
    """
    Test the edge cases around the login issue by checking if the login function returns the expected welcome message for valid credentials and raises the expected errors for invalid credentials.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"
    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)
    user = "test_user"
    password = ""
    with pytest.raises(ValueError):
        login(user, password)

def test_login_fix_existing_behaviour():
    """
    Test if the fix breaks existing expected behaviour by checking if the login function still returns the expected welcome message for valid credentials and raises the expected errors for invalid credentials.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"
    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)
    user = "test_user"
    password = ""
    with pytest.raises(ValueError):
        login(user, password)