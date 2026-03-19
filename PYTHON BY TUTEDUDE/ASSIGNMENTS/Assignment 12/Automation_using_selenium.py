from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open website
driver.get("https://quotes.toscrape.com")

time.sleep(2)

# Extract data
quotes = driver.find_elements(By.CLASS_NAME, "text")

for i, quote in enumerate(quotes, start=1):
    print(f"{i}: {quote.text}")

# Close browser
driver.quit()