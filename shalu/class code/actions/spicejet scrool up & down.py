import time

from idna.idnadata import scripts
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Initialize WebDriver
driver = webdriver.Chrome()


driver.get("https://www.spicejet.com/")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)
#scroll down
driver.execute_script("window.scrollBy(0,1000);")
time.sleep(5)
#scroll up
driver.execute_script("window.scrollBy(0,-1000);")
time.sleep(5)

element = driver.find_element(By.XPATH, "//*[@id='main-container']/div/div[1]/div[13]/div/div/div[1]/div[2]/div[1]/div")
driver.execute_script("arguments[0].scrollIntoView(true);",element)


time.sleep(5)

