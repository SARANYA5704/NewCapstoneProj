from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up headless Chrome
options = Options()
options.add_argument("--headless=new")  # Headless mode
options.add_argument("--no-sandbox")  # Required for GitHub Actions
options.add_argument("--disable-dev-shm-usage")  # Reduce resource usage

# Create driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Example: Open local Flask app
driver.get("http://127.0.0.1:5000")  # Flask runs on 127.0.0.1:5000
print(driver.title)

driver.quit()
