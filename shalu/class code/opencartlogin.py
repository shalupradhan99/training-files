from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Holland & Barrett login page

driver.get("https://demo.opencart.com/")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "username")
edit_box.send_keys("shalupradhan99@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("")
edit_box.send_keys(Keys.RETURN)

