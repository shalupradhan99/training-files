from anyio.abc import value
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v85.css import Value


driver = webdriver.Chrome()


driver.get("https://www.letskodeit.com/practice")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)
signin = driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/div').click()
time.sleep(3)
username = driver.find_element(By.ID, "email").send_keys("shalupradhan99@gmail.com")
password = driver.find_element(By.NAME, "password").send_keys("J4@Rb9iTr4R3Vm7")
login = driver.find_element(By.XPATH, value= '//*[@id="login"]').click()
time.sleep(5)
