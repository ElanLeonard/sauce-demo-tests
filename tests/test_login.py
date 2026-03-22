from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

def test_wrong_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "wrong_password")
    assert "Epic sadface" in login.get_error_message()

def test_locked_out_user(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.get_error_message()

def test_empty_fields(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "")
    assert "Username is required" in login.get_error_message()

def test_sql_injection(page):
    login = LoginPage(page)
    login.navigate()
    login.login("' OR '1'='1", "' OR '1'='1")
    assert "inventory" not in page.url
