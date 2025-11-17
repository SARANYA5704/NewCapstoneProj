import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_window_handling_privacy_policy_new_tab(driver):
    driver.get("https://practicesoftwaretesting.com/")
    time.sleep(2)

    # Scroll to footer
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Get the Privacy Policy link
    privacy_link = driver.find_element(By.LINK_TEXT, "Privacy Policy")

    # Extract its URL
    url = privacy_link.get_attribute("href")
    print("Opening URL:", url)

    parent_window = driver.current_window_handle
    print("Parent Window:", parent_window)

    # ⭐ Open the link in NEW TAB using JS
    driver.execute_script("window.open(arguments[0], '_blank');", url)
    time.sleep(2)

    # Get all windows
    all_windows = driver.window_handles
    print("All Windows:", all_windows)

    # Switch to the new tab
    for handle in all_windows:
        if handle != parent_window:
            driver.switch_to.window(handle)
            print("Switched to Child Tab")
            print("Child Title:", driver.title)
            print("Child URL:", driver.current_url)
            time.sleep(2)

            # Close child tab
            driver.close()
            print("Child Tab Closed")

            break

    # Back to parent tab
    driver.switch_to.window(parent_window)
    print("Back to Parent Tab:", driver.title)
    time.sleep(2)
