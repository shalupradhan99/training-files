import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Step 1: Launch the browser and open the URL
driver = webdriver.Chrome()
driver.get("https://www.hollandandbarrett.com/shop/vitamins-supplements/vitamins/")  # Replace with the correct URL
driver.maximize_window()
time.sleep(3)

ts1 = driver.find_element(By.TAG_NAME, value="img").get_attributes("src");
print(ts1)



links = driver.find_element(By.TAG_NAME, value="a")
for link in links:
    print(link.text)
    print(link.get_attribute("href"))