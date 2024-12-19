import time
from selenium import webdriver
from Open_Cart_POM1 import RegistrationPage  # Import the RegistrationPage class
from Open_Cart_POM2 import AccountPage  # Import the AccountPage class
from selenium.webdriver.common.by import By
class TestOpencartRegistration:
    def setup_method(self):
        # Step 1: Launch the browser and open the website
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.opencart.com.gr/")
        self.driver.maximize_window()
    def teardown_method(self):
        # Step 8: Close the browser after the test
        self.driver.quit()
    def test_registration(self):
        # Step 2: Navigate to Registration page
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        registration_page = RegistrationPage(self.driver)
        # Step 3: Verify the title (Page heading)
        assert self.driver.title == "Register Account"
        # Step 4: Fill in the registration details
        registration_page.fill_personal_details("Shalu", "pradhan", "will_smith123@gmail.com", "8945124534")
        # Step 5: Enter valid password
        registration_page.enter_password("willsmith@123")
        # Step 6: Agree to the privacy policy
        registration_page.agree_to_privacy_policy()
        # Step 7: Click 'Continue'
        registration_page.click_continue()
        # Step 8: Check if the "Privacy Policy" warning appears
        warning_msg = registration_page.get_warning_message()
        assert "Warning: You must agree to the Privacy Policy!" in warning_msg
        # Step 9: Agree to privacy policy, re-submit and check if account is created
        registration_page.agree_to_privacy_policy()
        registration_page.click_continue()
        time.sleep(2)  # Wait for the page to load
        # Step 10: Verify success message
        success_msg = registration_page.get_success_message()
        assert "Your Account Has Been Created!" in success_msg
        # Step 11: After account creation, view order history
        account_page = AccountPage(self.driver)
        account_page.click_order_history()
        time.sleep(2) # Wait for the page to load