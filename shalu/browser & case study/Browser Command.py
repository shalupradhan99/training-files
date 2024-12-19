from selenium import webdriver
import time

# URL to be opened
url = "http://automationpractice.com/index.php"

# Function to test the browser
def test_browser(driver):
    try:
        # Step 2: Open URL
        driver.get(url)
        time.sleep(2)  # Allow the page to load

        # Step 3: Get Page Title and Title length
        title = driver.title
        title_length = len(title)

        # Step 4: Print Page Title and Title length
        print(f"Page Title: {title}")
        print(f"Title Length: {title_length}")

        # Step 5: Get page URL and verify whether it is the desired page
        current_url = driver.current_url
        if current_url == url:
            print("URL Verified: The URL is correct.")
        else:
            print(f"URL Verification Failed: Expected {url}, but got {current_url}")

        # Step 6: Get Page Source and Page Source length
        page_source = driver.page_source
        page_source_length = len(page_source)

        # Step 7: Print Page Source length
        print(f"Page Source Length: {page_source_length}")
    finally:
        # Step 8: Close the browser
        driver.quit()
        print("Browser closed.")

# Main logic to choose a browser
print("Choose a browser:")
print("a. Chrome")
print("b. Edge")
print("c. Firefox")

choice = input("Enter your choice (a/b/c): ")

# Initialize the WebDriver based on user choice
driver = None
if choice == 'a':
    driver = webdriver.Chrome()
    print("Launching Chrome browser...").strip().lower()
elif choice == 'b':
    driver = webdriver.Edge()
    print("Launching Edge browser...")
elif choice == 'c':
    driver = webdriver.Firefox()
    print("Launching Firefox browser...")
else:
    print("Invalid choice. Please select a, b, or c.")
    exit()

# Call the test function
test_browser(driver)
#