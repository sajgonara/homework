from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    STANDARD_USER_BUTTON = (By.XPATH, "//android.widget.TextView[contains(@text, 'standard_user')]")
    USERNAME_FIELD = (By.ID, "Username")
    PASSWORD_FIELD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//*[@text='LOGIN']")

    def click_standard_user(self):
        self.logger.info("Attempting to click on standard_user element")
        self.click(self.STANDARD_USER_BUTTON)

    def enter_username(self, username: str):
        self.logger.info(f"Entering username: {username}")
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password: str):
        self.logger.info("Entering password")
        self.send_keys(self.PASSWORD_FIELD, password)

    def tap_login_button(self):
        self.logger.info("Tapping on the Login button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login_button()
