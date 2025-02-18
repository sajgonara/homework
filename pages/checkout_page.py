from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    LAST_NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    POSTAL_CODE_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    PAYMENT_INFO_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Payment Info")
    FINISH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")
    THANK_YOU_TEXT = (AppiumBy.XPATH, "//*[@text='THANK YOU FOR YOU ORDER']")

    def fill_personal_data(self, first_name: str, last_name: str, postal_code: str):
        self.send_keys(self.FIRST_NAME_FIELD, first_name)
        self.send_keys(self.LAST_NAME_FIELD, last_name)
        self.send_keys(self.POSTAL_CODE_FIELD, postal_code)

    def tap_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_thank_you_message(self):
        element = self.find(self.THANK_YOU_TEXT, timeout=10)
        return element.text