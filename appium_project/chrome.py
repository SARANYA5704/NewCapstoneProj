from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

print("🤖 Starting Google Search Test")

try:
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Medium_Phone"
    options.automation_name = "UiAutomator2"
    options.no_reset = True

    # Open Google App
    options.app_package = "com.google.android.googlequicksearchbox"
    options.app_activity = "com.google.android.googlequicksearchbox.SearchActivity"

    driver = webdriver.Remote("http://localhost:4723", options=options)
    print("✅ Google app opened!")
    time.sleep(3)

    # -------------------------
    # 1. CLICK SEARCH BOX
    # -------------------------
    try:
        search_box = driver.find_element(
            "xpath", "//android.widget.TextView[contains(@text,'Search') or contains(@text,'search')]"
        )
        search_box.click()
        print("✔ Search box clicked (XPath)")
    except:
        try:
            # tap the first clickable edit area
            input_field = driver.find_element("xpath", "//android.widget.EditText")
            input_field.click()
            print("✔ EditText clicked (fallback)")
        except:
            print("❌ No clickable search input found")

    time.sleep(2)

    # -------------------------
    # 2. TYPE SEARCH TEXT
    # -------------------------
    try:
        input_field = driver.find_element("xpath", "//android.widget.EditText")
        input_field.send_keys("https://www.flipkart.com/")
        print("✔ Typed search text")
        driver.keyevent(66) # ENTER
    except:
        print("❌ Could not type in search field")

    time.sleep(5)

    # Screenshot
    driver.save_screenshot("google_search.png")
    print("📸 Screenshot saved: google_search.png")

    driver.quit()
    print("✅ Test finished!")

except Exception as e:
    print(f"❌ Error: {e}")
