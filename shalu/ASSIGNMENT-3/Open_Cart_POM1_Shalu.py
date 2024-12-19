#URL:-https://demo.opencart.com.gr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
    # Locators for the registration form
    first_name = (By.ID, "input-firstname")
    last_name = (By.ID, "input-lastname")
    email = (By.ID, "input-email")
    telephone = (By.ID, "input-telephone")
    password = (By.ID, "input-password")
    confirm_password = (By.ID, "input-confirm")
    newsletter_yes = (By.XPATH, "//input[@name='newsletter'][@value='1']")
    privacy_policy = (By.XPATH, "//input[@name='agree']")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    warning_message = (By.CSS_SELECTOR, ".alert-danger")
    success_message = (By.CSS_SELECTOR, ".alert-success")
    # Method to fill in personal details
    def fill_personal_details(self, first_name_val, last_name_val, email_val, telephone_val):
        self.driver.find_element(*self.first_name).send_keys(first_name_val)
        self.driver.find_element(*self.last_name).send_keys(last_name_val)
        self.driver.find_element(*self.email).send_keys(email_val)
        self.driver.find_element(*self.telephone).send_keys(telephone_val)
    # Method to enter password and confirm password
    def enter_password(self, password_val):
        self.driver.find_element(*self.password).send_keys(password_val)
        self.driver.find_element(*self.confirm_password).send_keys(password_val)
    # Method to agree to the privacy policy
    def agree_to_privacy_policy(self):
        self.driver.find_element(*self.privacy_policy).click()
    # Method to click on 'Continue'
    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
    # Method to verify the warning message
    def get_warning_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.warning_message))
        return self.driver.find_element(*self.warning_message).text
    # Method to verify the success message
    def get_success_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message))
        return self.driver.find_element(*self.success_message).text