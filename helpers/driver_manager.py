from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config

class DriverManager:
    driver = None

    @classmethod
    def start_driver(cls):
        options = UiAutomator2Options()
        options.platform_name = Config.PLATFORM
        options.platform_version = Config.PLATFORM_VERSION
        options.device_name = Config.DEVICE_NAME
        options.app = Config.APP_PATH
        options.automation_name = Config.AUTOMATION_NAME

        options.app_activity = Config.APP_ACTIVITY
        options.app_wait_activity = Config.APP_WAIT_ACTIVITY

        options.set_capability("enforceXPath1", True)

        cls.driver = webdriver.Remote(Config.APPIUM_SERVER, options=options)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
