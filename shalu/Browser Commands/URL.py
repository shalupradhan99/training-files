import time

from selenium import webdriver

# Choose the browser (uncomment the one you want to use)
# For Chrome
# driver = webdriver.Chrome()  #4


# For Edge
# driver = webdriver.Edge()

# For Firefox
driver = webdriver.Firefox()

# Step 2: Open URL
url = "http://automationpractice.com/index.php"
driver.get(url)
time.sleep(5)

# Step 3: Get Page Title name and Title length
title = driver.title
title_length = len(title)

# Step 4: Print Page Title and Title length on the Console
print(f"Page Title: {title}")
print(f"Title Length: {title_length}")

# Step 5: Get page URL and verify whether it is the desired page or not
current_url = driver.current_url
if current_url == url:
    print("URL Verified: The URL is correct.")
else:
    print("URL Verification Failed: Incorrect URL.")

# Step 6: Get page Source and Page Source length
page_source = driver.page_source
page_source_length = len(page_source)

# Step 7: Print Page Source length on Console
print(f"Page Source Length: {page_source_length}")

# Step 8: Close the Browser
driver.quit()



