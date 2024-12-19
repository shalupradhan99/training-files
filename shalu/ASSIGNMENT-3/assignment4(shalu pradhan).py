from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver (use the appropriate driver for your browser)
driver = webdriver.Chrome()  # Replace with webdriver.Chrome() if using Chrome


# Step 1: Open the URL and Login with credentials
driver.get("http://demo.opencart.com.gr/")
driver.maximize_window()
time.sleep(2)

# Click on MyAccount button
driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
time.sleep(5)

# Select Login button
driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
time.sleep(5)

# Enter login credentials
driver.find_element(By.ID, "input-email").send_keys("will_smith123@gmail.com")  # Replace with valid email
driver.find_element(By.ID, "input-password").send_keys("willsmith@123")  # Replace with valid password
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(2)

# Step 2: Go to 'Components' tab and click
driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][normalize-space()='Components']").click()
time.sleep(2)

# Step 3: Select 'Monitors'
driver.find_element(By.XPATH, "//a[normalize-space()='Monitors (2)']").click()
time.sleep(2)

# Step 4: Select '25' from 'Show' dropdown
dropdown = Select(driver.find_element(By.ID, "input-limit"))
dropdown.select_by_visible_text("25")
time.sleep(2)

# Step 5: Click on 'Add to cart' for the first item
driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div[1]/div/div[2]/div[2]/button[1]").click()
time.sleep(2)

# Step 6: Click on 'Specification' tab
driver.find_element(By.LINK_TEXT, "Specification").click()
time.sleep(2)

# Step 7: Verify details present on the page (optional validation)
spec_details = driver.find_element(By.ID, "tab-specification").text
assert len(spec_details) > 0, "Specification details not found!"
print("Specification details verified!")

# Step 8: Click on 'Add to Wish List' button
driver.find_element(By.XPATH, "(//button[@data-original-title='Add to Wish List'])[1]").click()
time.sleep(3)

# Step 9: Verify success message
success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success: You have added" in success_message, "Add to Wish List failed!"
print("Add to Wish List success message verified!")
time.sleep(3)

# Step 10: Enter 'Mobile' in 'Search' textbox
driver.find_element(By.NAME, "search").send_keys("Mobile")
driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()
time.sleep(2)

# Step 11: Click on 'Search in product descriptions' checkbox
driver.find_element(By.ID, "description").click()
time.sleep(2)
dropdown = Select(driver.find_element(By.NAME, "category_id"))
dropdown.select_by_visible_text("Phones & PDAs")
time.sleep(3)
driver.find_element(By.ID, "button-search").click()
time.sleep(3)

# Step 12: Click on link 'HTC Touch HD'
driver.find_element(By.LINK_TEXT, "HTC Touch HD").click()
time.sleep(2)

# Step 13: Clear '1' from 'Qty' and enter '3'
qty_box = driver.find_element(By.ID, "input-quantity")
qty_box.clear()
qty_box.send_keys("3")
time.sleep(2)

# Step 14: Click on 'Add to Cart' button
driver.find_element(By.ID, "button-cart").click()
time.sleep(3)

# Step 15: Verify success message
success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success: You have added HTC Touch HD" in success_message, "Add to Cart failed!"
print("Add to Cart success message verified!")

# Step 16: Click on 'View Cart'
driver.find_element(By.LINK_TEXT, "shopping cart").click()
time.sleep(3)

# Step 17: Verify Mobile name added to the cart
cart_items = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[2]/a').text
assert "HTC Touch HD" in cart_items, "Item not found in the cart!"
print("Item verified in the cart!")

# Step 18: Click on 'Checkout' button
driver.find_element(By.LINK_TEXT, "Checkout").click()
time.sleep(2)

# Step 19: Logout
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(10)

# Step 20: Verify 'Account Logout' heading and click 'Continue'
logout_heading = driver.find_element(By.TAG_NAME, "h1").text
assert logout_heading == "Account Logout","Logout failed!"
print("Logout verified successfully!")
driver.find_element(By.LINK_TEXT, "Continue").click()


# Close the browser
driver.quit()