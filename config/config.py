import os
from dotenv import load_dotenv

load_dotenv()

# Normally I would leave here just the most common values that we use in our setup, but I went with what was the Android Studio default emulator ( the one that is set after the installation )

class Config:
    PLATFORM = os.getenv("PLATFORM", "Android")
    PLATFORM_VERSION = os.getenv("PLATFORM_VERSION", "11.0")
    DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")
    APP_PATH = os.getenv("APP_PATH", "/path/to/your/app.apk")
    APPIUM_SERVER = os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723")
    AUTOMATION_NAME = os.getenv("AUTOMATION_NAME", "UIAutomator2")
    APP_ACTIVITY = os.getenv("APP_ACTIVITY", "com.swaglabsmobileapp.MainActivity")
    APP_WAIT_ACTIVITY = os.getenv(
        "APP_WAIT_ACTIVITY",
        "com.swaglabsmobileapp.MainActivity, com.swaglabsmobileapp.SplashActivity"
    )
