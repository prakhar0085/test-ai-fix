import pytest
from auth import login, validate_password

def test_login_valid_credentials():
    """
    Test login function with valid credentials.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"

def test_login_none_username():
    """
    Test login function with None username.
    """
    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)

def test_login_none_password():
    """
    Test login function with None password.
    """
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)

def test_login_empty_password():
    """
    Test login function with empty password.
    """
    user = "test_user"
    password = ""
    with pytest.raises(ValueError):
        login(user, password)

def test_login_long_password():
    """
    Test login function with long password.
    """
    user = "test_user"
    password = "a" * 1000
    assert login(user, password) == f"Welcome, {user}!"

def test_login_password_with_special_chars():
    """
    Test login function with password containing special characters.
    """
    user = "test_user"
    password = "test_password!@#$"
    assert login(user, password) == f"Welcome, {user}!"

def test_validate_password_none():
    """
    Test validate_password function with None password.
    """
    password = None
    assert not validate_password(password)

def test_validate_password_empty():
    """
    Test validate_password function with empty password.
    """
    password = ""
    with pytest.raises(ValueError):
        validate_password(password)

def test_validate_password_valid():
    """
    Test validate_password function with valid password.
    """
    password = "test_password"
    assert validate_password(password)

def test_login_bug_fix():
    """
    Test the specific bug fix for the undefined username variable.
    """
    user = "test_user"
    password = "test_password"
    # The bug fix should prevent a NameError from occurring
    assert login(user, password) == f"Welcome, {user}!"

def test_login_edge_case_username_with_spaces():
    """
    Test login function with username containing spaces.
    """
    user = "test user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"

def test_login_edge_case_username_with_special_chars():
    """
    Test login function with username containing special characters.
    """
    user = "test_user!@#$"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"