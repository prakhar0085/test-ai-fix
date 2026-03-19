import pytest
from auth import login, validate_password

def test_login_with_alphanumeric_password():
    """
    Test login with alphanumeric password.
    """
    username = "john"
    password = "secret123"
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected

def test_login_with_password_containing_special_characters():
    """
    Test login with password containing special characters.
    """
    username = "john"
    password = "secret@123"
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected

def test_login_with_empty_password():
    """
    Test login with empty password.
    """
    username = "john"
    password = ""
    expected = "Login failed"
    assert login(username, password) == expected

def test_login_with_none_password():
    """
    Test login with None password.
    """
    username = "john"
    password = None
    with pytest.raises(TypeError):
        login(username, password)

def test_login_with_none_username():
    """
    Test login with None username.
    """
    username = None
    password = "secret123"
    with pytest.raises(TypeError):
        login(username, password)

def test_validate_password_with_alphanumeric_password():
    """
    Test validate_password with alphanumeric password.
    """
    password = "secret123"
    assert validate_password(password) == True

def test_validate_password_with_password_containing_special_characters():
    """
    Test validate_password with password containing special characters.
    """
    password = "secret@123"
    assert validate_password(password) == True

def test_validate_password_with_empty_password():
    """
    Test validate_password with empty password.
    """
    password = ""
    assert validate_password(password) == False

def test_validate_password_with_none_password():
    """
    Test validate_password with None password.
    """
    password = None
    assert validate_password(password) == False

def test_login_with_long_password():
    """
    Test login with long password.
    """
    username = "john"
    password = "a" * 1000
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected

def test_login_with_password_containing_non_ascii_characters():
    """
    Test login with password containing non-ASCII characters.
    """
    username = "john"
    password = "secret£123"
    expected = f"Welcome, {username}!"
    assert login(username, password) == expected