from selenium import webdriver
import time

# List of URLs to test
urls = [
    ("OrangeHRM", "https://opensource-demo.orangehrmlive.com/"),
    ("Opencart Demo", "https://demo.opencart.com/"),
    ("Guiding the way since 1860", "https://www.theaa.com/"),
    ("Cogmento Free CRM with AI Customer Relationship Management", "https://www.cogmento.com/"),
    ("Electronics, Cars, Fashion, Collectibles & More | eBay", "https://www.ebay.com/")
]

# Initialize Firefox WebDriver
driver = webdriver.Firefox()

try:
    for expected_title, url in urls:
        print(f"\n--- Testing URL: {url} ---")

        # Step 1: Launch Firefox and open URL
        driver.get(url)
        time.sleep(2)  # Allow the page to load

        # Step 2: Maximize the browser window
        driver.maximize_window()
        print("Browser maximized.")
        time.sleep(1)

        # Step 3: Minimize the browser window
        driver.minimize_window()
        print("Browser minimized.")
        time.sleep(1)

        # Step 4: Verify the title of the browser
        actual_title = driver.title
        print(f"Actual Title: {actual_title}")

        if expected_title.lower() in actual_title.lower():
            print("Title Verified: Title matches the expected title.")
        else:
            print(f"Title Mismatch: Expected '{expected_title}', but got '{actual_title}'")
finally:
    # Close the browser
    print("\nClosing the browser...")
    driver.quit()
