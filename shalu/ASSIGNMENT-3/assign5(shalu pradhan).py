import time

# import rows
from selenium import webdriver
from selenium.webdriver.common.by import By
import xutilites

# Initialize WebDriver
driver = webdriver.Chrome()
# driver.get("https://demo.opencart.com")
driver.get("https://demo.opencart.com.gr/")
driver.maximize_window()
time.sleep(5)
# driver.implicitly_wait(10)

# Path to the Excel file
path = r"C:\sps selenium\pythonProject\assignment3\UserDetails.xlsx"

# Get the row count from the Excel sheet
rows = xutilites.getRowCount(path, 'Sheet1')

# Iterate through the rows for login
for r in range(2, rows + 1):
    First_Name = xutilites.readData(path, "Sheet1", r, 1)  # Column 1 for username
    Last_Name = xutilites.readData(path, "Sheet1", r, 2)  # Column 2 for password
    Email = xutilites.readData(path, "Sheet1", r, 3)  # Column 3 for username
    Telephone = xutilites.readData(path, "Sheet1", r, 4)  # Column 4 for username
    Password = xutilites.readData(path, "Sheet1", r, 5)  # Column 5 for password
    Password_Confirm = xutilites.readData(path, "Sheet1", r, 6)  # Column 6 for password

    # Click on MyAccount button
    driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
    time.sleep(5)

    # Select Register button
    driver.find_element(By.XPATH, '//a[@href="https://demo.opencart.com.gr/index.php?route=account/register"]').click()
    time.sleep(5)

    # Validate the Register Account Text
    element = driver.find_element(By.XPATH, '//*[@id="content"]/h1')
    actual_text = element.text
    expected_text = "Account"

    if actual_text == expected_text:
        print("Text validation successful!")
    else:
        print(f"Text validation failed! Expected: '{expected_text}', but got: '{actual_text}'")

    # Wait for the First Name field to be visible and interactable
    time.sleep(2)  # Wait for a few seconds to ensure the elements are loaded
    fname_field = driver.find_element(By.ID, 'input-firstname')
    fname_field.clear()  # Clear any pre-filled text
    fname_field.send_keys(First_Name)

    # Wait for the Last Name field to be interactable
    time.sleep(2)  # Allow some time for the password field to load
    lname_field = driver.find_element(By.ID, 'input-lastname')
    lname_field.clear()  # Clear any pre-filled text
    lname_field.send_keys(Last_Name)

    # Wait for the Email field to be interactable
    time.sleep(2)  # Allow some time for the password field to load
    email_field = driver.find_element(By.ID, 'input-email')
    email_field.clear()  # Clear any pre-filled text
    email_field.send_keys(Email)

    # Wait for the Telephone field to be interactable
    time.sleep(2)  # Allow some time for the password field to load
    telephone_field = driver.find_element(By.ID, 'input-telephone')
    telephone_field.clear()  # Clear any pre-filled text
    telephone_field.send_keys(Telephone)

    # Wait for the Password field to be interactable
    time.sleep(2)  # Allow some time for the password field to load
    password_field = driver.find_element(By.ID, 'input-password')
    password_field.clear()  # Clear any pre-filled text
    password_field.send_keys(Password)

    # Wait for the Password Confirm field to be interactable
    time.sleep(2)  # Allow some time for the password field to load
    passwordcnf_field = driver.find_element(By.ID, 'input-confirm')
    passwordcnf_field.clear()  # Clear any pre-filled text
    passwordcnf_field.send_keys(Password_Confirm)

    # Click on Privacy policy check box
    driver.find_element(By.XPATH, '//input[@name="agree"]').click()
    time.sleep(5)

    # Click on Continue button
    driver.find_element(By.XPATH, '//input[@class="btn btn-primary"]').click()
    time.sleep(5)

    # Validate the Account Confirmation Text
    element_1 = driver.find_element(By.XPATH, '//*[@id="content"]/h1')
    actual_text = element_1.text
    expected_text = "Account"

    if actual_text == expected_text:
        print("Text validation successful!")
    else:
        print(f"Text validation failed! Expected: '{expected_text}', but got: '{actual_text}'")

    time.sleep(5)