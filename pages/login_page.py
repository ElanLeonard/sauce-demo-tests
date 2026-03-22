class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def get_error_message(self):
        return self.page.locator(".error-message-container").inner_text()