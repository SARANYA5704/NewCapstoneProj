from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
import time

print("🚀 Starting OrangeHRM Automation (No TouchAction)")

# ----------------------------------------------------
# ANDROID + CHROME OPTIONS
# ----------------------------------------------------
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("deviceName", "Medium_Phone")
options.set_capability("automationName", "UiAutomator2")

# Launch Chrome on device/emulator
options.set_capability("appium:appPackage", "com.android.chrome")
options.set_capability("appium:appActivity", "com.google.android.apps.chrome.Main")

# Auto-download correct Chromedriver for Chrome version
options.set_capability("appium:chromedriver_autodownload", True)

# Start driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.implicitly_wait(10)

# ----------------------------------------------------
# 1️⃣ OPEN ORANGE HRM SITE
# ----------------------------------------------------
url = "https://opensource-demo.orangehrmlive.com/"
print("🌐 Opening:", url)
driver.get(url)
time.sleep(4)

# ----------------------------------------------------
# 2️⃣ SEND KEYS (Username + Password)
# ----------------------------------------------------
print("⌨ Entering login credentials...")

try:
    driver.find_element(AppiumBy.NAME, "username").send_keys("Admin")
    driver.find_element(AppiumBy.NAME, "password").send_keys("admin123")
    print("✔ send_keys successful")
except:
    print("❌ send_keys failed")

time.sleep(2)

# ----------------------------------------------------
# 3️⃣ CLICK LOGIN BUTTON
# ----------------------------------------------------
print("🖱 Clicking Login Button...")

try:
    driver.find_element(AppiumBy.CSS_SELECTOR, "button[type='submit']").click()
    print("✔ Login button clicked")
except:
    print("❌ Login button not found")

time.sleep(4)

# ----------------------------------------------------
# 4️⃣ SCROLL DASHBOARD PAGE
# ----------------------------------------------------
print("📜 Scrolling Dashboard page...")

actions = ActionChains(driver)
actions.scroll_by_amount(0, 600).perform()

time.sleep(3)

# ----------------------------------------------------
# END OF TEST
# ----------------------------------------------------
print("🏁 Test Completed Successfully!")
driver.quit()
