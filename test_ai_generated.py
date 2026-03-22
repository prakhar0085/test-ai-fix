import pytest
from auth import validate_password, hash_password, login

def test_validate_password_with_special_characters():
    """
    Test that validate_password function returns True for passwords containing special characters.
    """
    password = "secret@123"
    assert validate_password(password) == True

def test_hash_password_with_special_characters():
    """
    Test that hash_password function correctly hashes passwords containing special characters.
    """
    password = "secret@123"
    hashed_password = hash_password(password)
    assert isinstance(hashed_password, str)

def test_login_with_password_containing_special_characters():
    """
    Test that login function successfully logs in with a password containing special characters.
    """
    username = "john"
    password = "secret@123"
    stored_password = hash_password(password)
    assert login(username, password, stored_password) == f"Welcome, {username}!"

def test_login_with_incorrect_password_containing_special_characters():
    """
    Test that login function fails to log in with an incorrect password containing special characters.
    """
    username = "john"
    password = "wrongpassword@123"
    stored_password = hash_password("secret@123")
    assert login(username, password, stored_password) == "Login failed"

def test_login_with_empty_password():
    """
    Test that login function raises a ValueError when the password is an empty string.
    """
    username = "john"
    password = ""
    stored_password = hash_password("secret@123")
    with pytest.raises(ValueError):
        login(username, password, stored_password)

def test_login_with_none_password():
    """
    Test that login function raises a TypeError when the password is None.
    """
    username = "john"
    password = None
    stored_password = hash_password("secret@123")
    with pytest.raises(TypeError):
        login(username, password, stored_password)

def test_login_with_none_username():
    """
    Test that login function raises a TypeError when the username is None.
    """
    username = None
    password = "secret@123"
    stored_password = hash_password("secret@123")
    with pytest.raises(TypeError):
        login(username, password, stored_password)

def test_hash_password_consistency():
    """
    Test that hash_password function consistently produces the same hash for the same password.
    """
    password = "secret@123"
    hashed_password1 = hash_password(password)
    hashed_password2 = hash_password(password)
    assert hashed_password1 == hashed_password2