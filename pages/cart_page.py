from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

class CartPage(BasePage):
    CART_ITEM_NAME = (By.ID, "test-cart-item-name")
    CHECKOUT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CHECKOUT")')
    CONTINUE_SHOPPING_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CONTINUE SHOPPING")')
    CART_ICON = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")

    def get_product_item(self, product_name: str):
        locator = (By.XPATH, f"//android.widget.TextView[contains(@text, '{product_name}')]")
        return self.find(locator)

    def tap_cart_icon(self):
        self.click(self.CART_ICON)

    def get_cart_item_name(self):
        return self.find(self.CART_ITEM_NAME).text

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def remove_item(self, product_name: str):
        locator = (By.XPATH, f"//android.widget.TextView[contains(@text, '{product_name}')]/following::*[@text='REMOVE'][1]")
        self.click(locator)