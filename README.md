# Mobile App Test Automation Framework task for Inpost

This repository contains a simple test automation framework for a native mobile application. It uses **Appium 2.15.0** and **pytest**.

## Requirements

- Appium 2.15.0
- Python 3.x
- Android SDK (for Android tests) or Xcode (for iOS tests)
- A configured device/emulator
- Java JDK (required for Android automation)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <project-folder>

2. **Create and activate a virtual environment:**
   ```bash 
   python -m venv venv
   source venv/bin/activate      # On Unix/MacOS
   venv\Scripts\activate         # On Windows

3. **Install dependencies (pip or pip3):**
   ```bash 
   pip install -r requirements.txt

4. **Configure environment variables:**
   - Rename the provided .env.example file to .env
   - Update the file with your configuration details (e.g., PLATFORM, PLATFORM_VERSION, DEVICE_NAME, APP_PATH, APPIUM_SERVER, etc.)

## Running the Tests

1. **Run Appium:**
   ```bash 
   appium

2. **Run the tests:**
   ```bash 
   pytest --maxfail=1 --disable-warnings -q

