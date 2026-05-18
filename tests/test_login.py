from pages.login_page import LoginPage

def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.page.url

def test_wrong_password(login_page):
    login_page.login("standard_user", "wrong_password")
    assert "Epic sadface" in login_page.get_error_message()

def test_locked_out_user(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.get_error_message()

def test_empty_fields(login_page):
    login_page.login("", "")
    assert "Username is required" in login_page.get_error_message()

def test_sql_injection(login_page):
    login_page.login("' OR '1'='1", "' OR '1'='1")
    assert login_page.get_error_message() != ""

def test_product_header_present(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "Product" in login_page.get_page_title()

