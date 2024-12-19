from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the URL in the Chrome browser
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Step 2: Wait for the page to load
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='alertbtn']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='confirmbtn']").click()
time.sleep(5)
# Close the browser
driver.quit()
