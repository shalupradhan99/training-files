import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Step 1: Launch the browser and open the URL
driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en/")  # Replace with the correct URL
driver.maximize_window()
time.sleep(3)

all_links = driver.find_element(By.XPATH, value =".//a")
print(len(all_links))

for links in all_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link present")
    else:
        print("link not present")
footer_links = driver.find_element(By.XPATH, value=".//div[@class='footer-upper-wrapper']//a")
print(len(footer_links))

for links in footer_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link present")
    else:
        print("link not present")

