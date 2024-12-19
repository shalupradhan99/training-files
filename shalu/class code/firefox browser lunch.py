from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(8)
actual_title = driver.title
expect_title="sign in to your account"
if actual_title == expect_title:
    print("login is successfully")
else:
    print("login unsuccess")