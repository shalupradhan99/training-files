from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v85.css import Value


driver = webdriver.Chrome()

# Open the Holland & Barrett login page
driver.get("https://auth.hollandandbarrett.com/u/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("shalupradhan99@gmail.com")
driver.find_element(By.NAME, "password").send_keys("GdSJhj*b.nL6gSN")
driver.find_element(By.XPATH, value = '/html/body/main/section/div/div/div/form/div[2]/button').click()
time.sleep(5)