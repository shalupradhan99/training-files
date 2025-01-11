from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.easycalculation.com/index.php#google_vignette")
time.sleep(3)

driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[2]/div[2]/span[2]/a[1]/span[1]").click()
time.sleep(2)

driver.find_element(By.ID,"log_email").send_keys("dadakhalendar143@gmail.com")
driver.find_element(By.NAME, "log_password").send_keys("dadu@123")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/div[4]/input[1]").click()
time.sleep(5)

driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/form[1]/span[1]/input[1]").click()
driver.find_element(By.ID,"googleSearchId" ).send_keys("Bangalore")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/form[1]/span[2]/button[1]").click()
time.sleep(3)

driver.get("https://www.easycalculation.com/budget/living-cost-Bangalore-India-to-San_Francisco_CA-United_States.html")
time.sleep(3)

driver.quit()
