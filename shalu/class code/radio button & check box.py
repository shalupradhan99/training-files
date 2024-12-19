from tkinter import Radiobutton

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the URL in the Chrome browser
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Step 2: Wait for the page to load
time.sleep(5)
bmwRadiobutton =driver.find_element(By.ID, "bmwradio")
bmwRadiobutton.click()
time.sleep(5)
benzRadioBtn =driver.find_element(By.ID, "benzradio")
benzRadioBtn.click()
time.sleep(5)
bmwCheckbox =driver.find_element(By.ID, "bmwcheck")
bmwCheckbox.click()
time.sleep(5)
benzCheckbox =driver.find_element(By.ID, "benzcheck")
benzCheckbox.click()
time.sleep(5)
print("bmw radio button is selected?"+str(bmwRadiobutton.is_selected()))
print("bmw radio button is selected?"+str(benzRadioBtn.is_selected()))
print("bmw radio button is selected?"+str(bmwCheckbox.is_selected()))
print("bmw radio button is selected?"+str(benzCheckbox.is_selected()))
