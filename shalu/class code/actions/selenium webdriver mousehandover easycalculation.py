import time

from idna.idnadata import scripts
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Initialize WebDriver
driver = webdriver.Chrome()


driver.get("https://www.easycalculation.com/#google_vignette")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

element=driver.find_element(By.CLASS_NAME,value="nav-anchor")
itemToClickLocator ="/html[1]/body[1]/div[1]/header[1]/div[1]/div[2]/div[1]/span[2]/div[1]/ul[1]/li[3]/a[1]/span[2]"

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
