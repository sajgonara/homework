from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "Username")
    PASSWORD_FIELD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//*[@text='LOGIN']")
    STANDARD_USER_BUTTON = (By.XPATH, "//android.widget.TextView[@text='standard_user']")

    def click_standard_user(self):
        self.click(self.STANDARD_USER_BUTTON)

    def enter_username(self, username: str):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password: str):
        self.send_keys(self.PASSWORD_FIELD, password)

    def tap_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login_button()
