from selenium import webdriver

# Define URLs and their expected titles
urls = [
    ("OrangeHRM", "https://demo.opencart.com/"),
    ("Guiding the way since 1860", "https://www.theaa.com/"),
    ("Cogmento Free CRM with AI Customer Relationship Management", "https://www.cogmento.com/"),
    ("Electronics, Cars, Fashion, Collectibles & More | eBay", "https://www.ebay.com/")
]

# Choose the browser (uncomment the one you want to use)
# Chrome
# driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Edge
# driver = webdriver.Edge(executable_path='path/to/edgedriver')

# Firefox
driver = webdriver.Firefox()

# Iterate through each URL
for expected_title, url in urls:
    print(f"\n--- Processing URL: {url} ---")
    driver.get(url)

    # Step 3: Get Page Title name and Title length
    title = driver.title
    title_length = len(title)

    # Step 4: Print Page Title and Title length
    print(f"Page Title: {title}")
    print(f"Title Length: {title_length}")

    # Step 5: Get page URL and verify
    current_url = driver.current_url
    if current_url == url:
        print("URL Verified: The URL is correct.")
    else:
        print(f"URL Verification Failed: Expected {url}, but got {current_url}")

    # Step 6: Get page Source and its length
    page_source = driver.page_source
    page_source_length = len(page_source)

    # Step 7: Print Page Source length
    print(f"Page Source Length: {page_source_length}")
    print(f"Expected Title: {expected_title}, Actual Title: {title}")

# Step 8: Close the browser
driver.quit()
