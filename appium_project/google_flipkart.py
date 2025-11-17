from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("🤖 Starting Flipkart Automation Test")

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
    # 1. CLICK GOOGLE SEARCH BOX
    # -------------------------
    try:
        search_box = driver.find_element(
            "xpath", "//android.widget.TextView[contains(@text,'Search') or contains(@text,'search')]"
        )
        search_box.click()
        print("✔ Search box clicked (XPath)")
    except:
        try:
            input_field = driver.find_element("xpath", "//android.widget.EditText")
            input_field.click()
            print("✔ EditText clicked (fallback)")
        except:
            print("❌ No clickable search input found")

    time.sleep(2)

    # -------------------------
    # 2. TYPE GOOGLE SEARCH: Flipkart
    # -------------------------
    try:
        input_field = driver.find_element("xpath", "//android.widget.EditText")
        input_field.send_keys("https://www.flipkart.com/")
        print("✔ Typed 'Flipkart'")
        driver.press_keycode(66)  # ENTER
    except:
        print("❌ Could not type in search field")

    time.sleep(5)

    # -------------------------
    # 4. SWITCH TO WEBVIEW
    # -------------------------
    contexts = driver.contexts
    webview = None
    for context in contexts:
        if "WEBVIEW" in context:
            webview = context
            break

    if webview:
        driver.switch_to.context(webview)
        print("✔ Switched to WebView for Flipkart website")
    else:
        print("❌ WebView context not found")
        driver.quit()
        exit()

    time.sleep(5)

    # -------------------------
    # 5. SEARCH iPhone 15 ON FLIPKART
    # -------------------------
    try:
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.click()
        search_box.clear()
        search_box.send_keys("iPhone 15")
        search_box.submit()  # Press enter
        print("🔍 Typed 'iPhone 15' in Flipkart search bar")
    except:
        print("❌ Could not find Flipkart search bar")
        driver.quit()
        exit()

    time.sleep(8)

    # -------------------------
    # 6. CLICK FIRST PRODUCT
    # -------------------------
    try:
        first_product = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//a[contains(@href,'/apple-iphone-15')])[1]")
            )
        )
        first_product.click()
        print("📱 First iPhone 15 clicked")
    except:
        print("❌ Could not click first iPhone 15 product")
        driver.quit()
        exit()

    time.sleep(6)

    # -------------------------
    # 7. CLICK ADD TO CART
    # -------------------------
    try:
        add_to_cart = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Add to Cart')]")
            )
        )
        add_to_cart.click()
        print("🛒 Add to Cart clicked!")
    except:
        print("❌ Add to Cart button not found")

    time.sleep(5)

    # Screenshot
    driver.save_screenshot("flipkart_iphone15_cart.png")
    print("📸 Screenshot saved: flipkart_iphone15_cart.png")

    driver.quit()
    print("✅ Test finished!")

except Exception as e:
    print(f"❌ Error: {e}")
