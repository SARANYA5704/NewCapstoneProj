from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

print("🚀 Starting headless test...")

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open a website
    driver.get("https://www.google.com")
    print("Title of page:", driver.title)

    # Perform a simple search
    search_box = driver.find_element("name", "q")
    search_box.send_keys("OpenAI")
    search_box.submit()

    # Wait a few seconds for results
    driver.implicitly_wait(5)

    # Print first result title
    first_result = driver.find_element("css selector", "h3")
    print("First result:", first_result.text)

finally:
    driver.quit()
    print("✅ Headless test finished.")
