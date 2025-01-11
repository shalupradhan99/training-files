import time

from idna.idnadata import scripts
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Initialize WebDriver
driver = webdriver.Chrome()


driver.get("https://www.rajasthanroyals.com/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

element=driver.find_element(By.CLASS_NAME,value="nav-anchor")
itemToClickLocator ="//span[normalize-space()='Squad']"

try:
    actions= ActionChains(driver)
    actions.move_to_element(element).perform()
    print("mouse handovered on 'squid' element")
    time.sleep(5)
    topLink = driver.find_element(By.XPATH,itemToClickLocator)
    actions.move_to_element(topLink).click().perform()

    print("item clicked")
except:
    print("mouse hover failed on element")

