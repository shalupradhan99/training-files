import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class AccountPage:
    def __init__(self, driver):
        self.driver = driver
    # Locator for the 'View your Order history' link
    order_history_link = (By.LINK_TEXT, "View your order history")
    def click_order_history(self):
        self.driver.find_element(*self.order_history_link).click()
