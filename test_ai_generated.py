import pytest
from auth import login, validate_password

def test_login_valid_credentials():
    """
    Test login with valid credentials.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"

def test_login_none_username():
    """
    Test login with None username.
    """
    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)

def test_login_none_password():
    """
    Test login with None password.
    """
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)

def test_login_empty_password():
    """
    Test login with empty password.
    """
    user = "test_user"
    password = ""
    with pytest.raises(ValueError):
        login(user, password)

def test_login_long_password():
    """
    Test login with long password.
    """
    user = "test_user"
    password = "a" * 1000
    assert login(user, password) == f"Welcome, {user}!"

def test_validate_password_none():
    """
    Test validate_password with None password.
    """
    password = None
    assert not validate_password(password)

def test_validate_password_empty():
    """
    Test validate_password with empty password.
    """
    password = ""
    with pytest.raises(ValueError):
        validate_password(password)

def test_validate_password_valid():
    """
    Test validate_password with valid password.
    """
    password = "test_password"
    assert validate_password(password)

def test_bug_fix_specific():
    """
    Test the specific bug fix by checking if the function raises a TypeError when either user or password is None.
    """
    user = "test_user"
    password = None
    with pytest.raises(TypeError):
        login(user, password)

    user = None
    password = "test_password"
    with pytest.raises(TypeError):
        login(user, password)

def test_fix_doesnt_break_existing_behaviour():
    """
    Test that the fix doesn't break existing expected behaviour by checking if the function returns the expected result for valid credentials.
    """
    user = "test_user"
    password = "test_password"
    assert login(user, password) == f"Welcome, {user}!"