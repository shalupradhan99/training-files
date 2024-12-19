from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the path to your ChromeDriver if necessary
driver.maximize_window()
# Open the Holland & Barrett login page
driver.get("https://auth.hollandandbarrett.com/u/login")

# Wait for the page to load
time.sleep(8)

# Get and verify the title of the page
expected_title = "Login - Holland & Barrett"  # Replace with the correct expected title
actual_title = driver.title

if actual_title == expected_title:
    print("Login is successful . . . . . Well done Python ")
else:
    print("Login Unsuccessful . . . . . Very good my boy")

# Close the driver after use
driver.quit()