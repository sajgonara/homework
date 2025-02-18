from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.logger import setup_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = setup_logger(self.__class__.__name__)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator, timeout=10):
        element = self.find(locator, timeout)
        self.logger.info(f"Clicking on element: {locator}")
        element.click()

    def send_keys(self, locator, text, timeout=10):
        element = self.find(locator, timeout)
        self.logger.info(f"Sending keys '{text}' to element: {locator}")
        element.clear()
        element.send_keys(text)

    def swipe_up(self, duration=800):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        start_x = int(width * 0.5)
        start_y = int(height * 0.8)
        end_y = int(height * 0.2)

        touch_input = PointerInput("touch", "touch")
        actions = ActionBuilder(self.driver)
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()

    def build_xpath_by_text(self, text: str, tag: str = "android.widget.TextView") -> tuple:
        xpath = f"//{tag}[contains(@text, '{text}')]"
        return (By.XPATH, xpath)
