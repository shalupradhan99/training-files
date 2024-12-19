from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Step 1: Open Flipkart
    driver.get("https://www.flipkart.com/")
    time.sleep(5)

    # Close login popup if it appears
    try:
        close_popup = driver.find_element(By.XPATH, "//a[@class='wsejfv']")
        close_popup.click()
    except:
        pass  # If popup doesn't appear, continue

    # Locate the "Fashion" menu
    fashion_menu = driver.find_element(By.XPATH, "//div[@aria-label='Fashion']//div//span[@class='_1XjE3T']")

    # Initialize ActionChains
    actions = ActionChains(driver)

    # Hover over the "Fashion" menu
    actions.move_to_element(fashion_menu).perform()

    # Wait for the dropdown to appear
    time.sleep(5)

    # Step 2: Click on "Women Ethnic"
    women_ethnic_option = driver.find_element(By.XPATH, "//a[text()='Women Ethnic']")
    actions.move_to_element(women_ethnic_option).perform()

    # Wait for the sub-menu to appear
    time.sleep(5)

    # Step 3:Click on "Women Sarees"
    women_sarees_option = driver.find_element(By.XPATH, "//a[text()='Women Sarees']")
    women_sarees_option.click()

    # Step 4: Take a screenshot
    screenshot_path = "flipkart_saree_list.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

    # Step 5: Select 'Bollywood Saree' from filters
    saree_type = driver.find_element(By.XPATH, "//body/div[@id='container']/div/div[@class='JxFEK3 _48O0EI']/div[@class='DOjaWF YJG4Cf col-12-12']/div[@class='cPHDOP col-2-12']/div[@class='_0BvurA']/section[7]/div[1]")
    saree_type.click()
    time.sleep(5)

    select_bollywood = driver.find_element(By.XPATH, "//div[@title='Bollywood']//div[@class='XqNaEv']")
    select_bollywood.click()
    time.sleep(5)

    # Step 6: Click on some random saree in the list
    random_saree = driver.find_element(By.XPATH, "//div[5]//div[1]//div[2]//div[1]//div[1]//a[1]")
    random_saree.click()
    time.sleep(8)

    # Switch to the new tab where the saree details are opened
    driver.switch_to.window(driver.window_handles[1])

    # Step 7: Click 'Add to Cart'
    add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button.click()
    time.sleep(3)

    # Step 8: Take a screenshot
    screenshot_path = "flipkart_add_to_cart.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

    # Step 9: Click 'Place Order'
    place_order_button = driver.find_element(By.XPATH, "//span[normalize-space()='Place Order']")
    place_order_button.click()
    time.sleep(3)

    # Step 10: Enter mobile number and continue
    mobile_input = driver.find_element(By.XPATH, "//input[@type='text' and @autocomplete='off']")
    mobile_input.send_keys("9178251492")  # Replace with a valid number
    time.sleep(1)

    continue_button = driver.find_element(By.XPATH, "//span[text()='CONTINUE']")
    continue_button.click()
    time.sleep(3)

    # Step 11: Take a screenshot
    screenshot_path = "flipkart_order_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Step 12: Close the browser
    driver.quit()