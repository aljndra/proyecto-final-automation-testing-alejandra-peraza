import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False)
])
def test_login(driver, username, password, expected):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    
    home_page = HomePage(driver)
    if expected:
        assert home_page.is_displayed()
    else:
        assert login_page.get_error_message() != ""
