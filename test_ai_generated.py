import pytest
from auth import login, validate_password

def test_login_empty_password():
    """
    Test that login function raises ValueError when password is an empty string.
    """
    with pytest.raises(ValueError):
        login("alice", "")

def test_login_none_password():
    """
    Test that login function raises TypeError when password is None.
    """
    with pytest.raises(TypeError):
        login("alice", None)

def test_login_none_user():
    """
    Test that login function raises TypeError when user is None.
    """
    with pytest.raises(TypeError):
        login(None, "password123")

def test_login_whitespace_password():
    """
    Test that login function raises ValueError when password contains only whitespace characters.
    """
    with pytest.raises(ValueError):
        login("alice", "   ")

def test_login_valid_user():
    """
    Test that login function returns a welcome message when user and password are valid.
    """
    assert login("alice", "password123") == "Welcome, alice!"

def test_login_valid_user_with_numbers():
    """
    Test that login function returns a welcome message when user contains numbers and password is valid.
    """
    assert login("alice123", "password123") == "Welcome, alice123!"

def test_login_valid_user_with_special_chars():
    """
    Test that login function returns a welcome message when user contains special characters and password is valid.
    """
    assert login("alice!", "password123") == "Welcome, alice!!"

def test_login_long_password():
    """
    Test that login function returns a welcome message when password is long.
    """
    assert login("alice", "password1234567890") == "Welcome, alice!"

def test_login_short_password():
    """
    Test that login function returns a welcome message when password is short.
    """
    assert login("alice", "pass") == "Welcome, alice!"

def test_validate_password_valid():
    """
    Test that validate_password function returns True when password is valid.
    """
    assert validate_password("password123") == True

def test_validate_password_empty():
    """
    Test that validate_password function raises ValueError when password is an empty string.
    """
    with pytest.raises(ValueError):
        validate_password("")

def test_validate_password_none():
    """
    Test that validate_password function raises ValueError when password is None.
    """
    with pytest.raises(ValueError):
        validate_password(None)

def test_validate_password_whitespace():
    """
    Test that validate_password function raises ValueError when password contains only whitespace characters.
    """
    with pytest.raises(ValueError):
        validate_password("   ")