import pytest
from auth import login, validate_password

def test_validate_password_typo_fix():
    """
    Test that the validate_password function no longer raises a NameError due to the typo.
    """
    password = "test_password"
    assert validate_password(password) == True

def test_login_typo_fix():
    """
    Test that the login function no longer raises a NameError due to the typo.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"

def test_login_valid_credentials():
    """
    Test that the login function returns the expected message for valid credentials.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"

def test_login_none_username():
    """
    Test that the login function raises a TypeError for None username.
    """
    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)

def test_login_none_password():
    """
    Test that the login function raises a TypeError for None password.
    """
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)

def test_login_empty_password():
    """
    Test that the login function raises a ValueError for empty password.
    """
    user = "test_user"
    password = ""
    with pytest.raises(ValueError):
        login(user, password)

def test_login_long_password():
    """
    Test that the login function returns the expected message for a long password.
    """
    user = "test_user"
    password = "a" * 100
    assert login(user, password) == f"Welcome, {user}!"

def test_login_password_with_special_characters():
    """
    Test that the login function returns the expected message for a password with special characters.
    """
    user = "test_user"
    password = "test_password!@#$"
    assert login(user, password) == f"Welcome, {user}!"

def test_validate_password_none():
    """
    Test that the validate_password function returns False for None password.
    """
    password = None
    assert validate_password(password) == False

def test_validate_password_empty():
    """
    Test that the validate_password function raises a ValueError for empty password.
    """
    password = ""
    with pytest.raises(ValueError):
        validate_password(password)

def test_validate_password_valid():
    """
    Test that the validate_password function returns True for a valid password.
    """
    password = "test_password"
    assert validate_password(password) == True