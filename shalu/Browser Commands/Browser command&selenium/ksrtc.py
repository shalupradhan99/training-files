from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ksrtc.in/login")
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='btn payee']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='okayButton']").click()
time.sleep(5)