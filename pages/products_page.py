from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    # Example how we can use dynamic locators based on a passed parameter, normally I would go with a more complex helper method like LocatorFactory or similar, but I didn't want to make an overkill on a simple app
    def add_product_to_cart(self, product_name: str):
        base_locator = self.build_xpath_by_text(product_name)
        final_xpath = f"{base_locator[1]}/following::*[@text='ADD TO CART'][1]"
        self.click((By.XPATH, final_xpath))

    def add_backpack_to_cart(self):
        self.click(self.SAUCE_LABS_BACKPACK_ADD_TO_CART)

    def open_cart(self):
        self.click(self.CART_ICON)
