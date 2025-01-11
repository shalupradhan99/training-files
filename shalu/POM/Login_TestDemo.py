from selenium import webdriver
import time
from POM.Login_Page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        # Set up the test environment
        baseURL = "https://auth.hollandandbarrett.com/u/login"
        driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or use webdriver-manager
        driver.maximize_window()
        driver.get(baseURL)
        time.sleep(5)  # Consider replacing this with explicit waits for better performance

        # Initialize LoginPage object
        lp = LoginPage(driver)

        # Perform login
        lp.login(email="shalupradhan99@gmail.com", password="J4@Rb9iTr4R3Vm7")

        # Verify the title
        actual_title = driver.title
        expect_title = "Sign in - to your account, for the best experience"

        if actual_title == expect_title:
            print("Login is successful.....well done python")
        else:
            print("Login unsuccessful... very good my boy!")

        # Close the browser
        driver.quit()

if __name__ == "__main__":
    unittest.main()

