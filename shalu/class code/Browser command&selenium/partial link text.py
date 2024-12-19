import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Step 1: Launch the browser and open the URL
driver = webdriver.Chrome()
driver.get("https://www.hollandandbarrett.com/")  # Replace with the correct URL
driver.maximize_window()
time.sleep(5)

partial_link="Vitamins"
link_element=driver.find_element(By.PARTIAL_LINK_TEXT,partial_link)
link_element.click()
time.sleep(5)