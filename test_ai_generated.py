import pytest
from auth import login, validate_password

def test_login_with_empty_password():
    """
    Test login with empty password.
    
    This test case checks if the login function raises a ValueError when an empty string is passed as the password.
    """
    username = "john"
    password = ""
    with pytest.raises(ValueError):
        login(username, password)

def test_login_with_none_password():
    """
    Test login with None password.
    
    This test case checks if the login function raises a TypeError when None is passed as the password.
    """
    username = "john"
    password = None
    with pytest.raises(TypeError):
        login(username, password)

def test_login_with_none_username():
    """
    Test login with None username.
    
    This test case checks if the login function raises a TypeError when None is passed as the username.
    """
    username = None
    password = "secret123"
    with pytest.raises(TypeError):
        login(username, password)

def test_login_with_valid_credentials():
    """
    Test login with valid credentials.
    
    This test case checks if the login function returns the expected welcome message when valid credentials are provided.
    """
    username = "john"
    password = "secret123"
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected

def test_login_with_long_password():
    """
    Test login with long password.
    
    This test case checks if the login function handles long passwords correctly.
    """
    username = "john"
    password = "a" * 1000
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected

def test_login_with_password_containing_special_characters():
    """
    Test login with password containing special characters.
    
    This test case checks if the login function handles passwords with special characters correctly.
    """
    username = "john"
    password = "secret@123"
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected

def test_login_with_password_containing_non_ascii_characters():
    """
    Test login with password containing non-ASCII characters.
    
    This test case checks if the login function handles passwords with non-ASCII characters correctly.
    """
    username = "john"
    password = "secret£123"
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected

def test_validate_password_with_empty_password():
    """
    Test validate_password with empty password.
    
    This test case checks if the validate_password function raises a ValueError when an empty string is passed as the password.
    """
    password = ""
    with pytest.raises(ValueError):
        validate_password(password)

def test_validate_password_with_none_password():
    """
    Test validate_password with None password.
    
    This test case checks if the validate_password function returns False when None is passed as the password.
    """
    password = None
    assert validate_password(password) == False

def test_validate_password_with_valid_password():
    """
    Test validate_password with valid password.
    
    This test case checks if the validate_password function returns True when a valid password is provided.
    """
    password = "secret123"
    assert validate_password(password) == True

def test_validate_password_with_long_password():
    """
    Test validate_password with long password.
    
    This test case checks if the validate_password function handles long passwords correctly.
    """
    password = "a" * 1000
    assert validate_password(password) == True

def test_validate_password_with_password_containing_special_characters():
    """
    Test validate_password with password containing special characters.
    
    This test case checks if the validate_password function handles passwords with special characters correctly.
    """
    password = "secret@123"
    assert validate_password(password) == True

def test_validate_password_with_password_containing_non_ascii_characters():
    """
    Test validate_password with password containing non-ASCII characters.
    
    This test case checks if the validate_password function handles passwords with non-ASCII characters correctly.
    """
    password = "secret£123"
    assert validate_password(password) == True