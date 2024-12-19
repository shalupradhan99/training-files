import time

from anyio.abc import value
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch the browser and open the URL
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")  # Replace with the correct URL
driver.maximize_window()
time.sleep(3)  # Allow the page to load

try:
    # Step 2: Click on the "Sign In" button
    signin_button = driver.find_element(By.XPATH, "//a[@class='login']")
    signin_button.click()
    time.sleep(2)

    # Step 3: Enter email and password, then click "Sign In"
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("ridhishapradhan19@gmail.com")  # Replace with valid credentials

    password_field = driver.find_element(By.NAME, "passwd")
    password_field.send_keys("Momdad@506")  # Replace with valid credentials

    login_button = driver.find_element(By.ID, "SubmitLogin")
    login_button.click()
    time.sleep(3)

    # Step 4: Click on "Dresses" link, then click on "Women"
    dresses_link = driver.find_element(By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a")

    dresses_link.click()
    time.sleep(2)

    women_link = driver.find_element(By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")
    women_link.click()
    time.sleep(5)

finally:
    # Step 5: Close the browser
    driver.quit()
