import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://auth.hollandandbarrett.com/u/login")
    driver.maximize_window()
    time.sleep(5)

    # Locate username field and input text
    driver.find_element(By.ID, "username").send_keys("shalupradhan99@gmail.com")

    # Locate password field and input text
    driver.find_element(By.NAME, "password").send_keys("GdSJhj*b.nL6gSN")
    time.sleep(5)

finally:
    # Close the browser after completion
    driver.quit()
