from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v85.css import Value

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Holland & Barrett login page
driver.get("https://auth.hollandandbarrett.com/u/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "username")
edit_box.send_keys("shalupradhan99@gmail.com")

edit_box.send_keys(Keys.RETURN)
time.sleep(5)
edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("GdSJhj*b.nL6gSN")
edit_box.send_keys(Keys.RETURN)
edit_box = driver.find_element(By.XPATH, value = '/html/body/main/section/div/div/div/form/div[2]/button').click()
time.sleep(5)
