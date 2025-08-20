from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Path to chromedriver
service = Service("C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Step 1: Open AUT
driver.get("https://www.saucedemo.com/")

# Step 2: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 3: Search functionality (simulated by checking product list)
search_product = "Sauce Labs Backpack"
items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

found = False
for item in items:
    if search_product in item.text:
        found = True
        print("✅ Product found in search results:", item.text)
        break

if not found:
    print("❌ Product not found in search results")

time.sleep(2)
driver.quit()
