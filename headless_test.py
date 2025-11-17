from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("🚀 Starting simple headless Selenium test...")

# Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open a static website
    driver.get("https://example.com")  # This is a simple, stable page
    print("Page title:", driver.title)

    # Extract header text (h1)
    header = driver.find_element(By.TAG_NAME, "h1")
    print("Header text:", header.text)

finally:
    driver.quit()
    print("✅ Simple headless test finished.")

