from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
time.sleep(2)
driver.switch_to.alert.accept()
result = driver.find_element(By.ID,'result').text
print("value of attribute is:" +result)
assert "You successfully clicked an alert", result

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(2)
driver.switch_to.alert.accept()
result = driver.find_element(By.ID,'result').text
print("value of attribute is:" +result)
assert "You clicked: Ok", result

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
result = driver.find_element(By.ID,'result').text
print("value of attribute is:" +result)
assert "You clicked: Cancel", result

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Good morning Shalu")
driver.switch_to.alert.accept()
result = driver.find_element(By.ID,'result').text
print("value of attribute is:" +result)
assert "You entered: Good morning Shalu", result

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
val = driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! You must have the proper credentials')]").text
time.sleep(3)
print("value of attribute is:" + val)
assert "'Congratulations! you must have the proper credentials.", val
