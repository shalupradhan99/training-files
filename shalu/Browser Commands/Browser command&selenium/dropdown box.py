from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/campaign/landing.php")
time.sleep(5)

dropdown=driver.find_element(By.ID,'month')
select=Select(dropdown)
time.sleep(5)

num_options = len(select.options)
print(f"There are {num_options} options in the month dropdown")

for option in select.options:
    print(option.text)