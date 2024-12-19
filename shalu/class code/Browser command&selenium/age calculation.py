from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize browser drivers for Chrome and Edge
def init_browser(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        return webdriver.Chrome()
    elif browser_name.lower() == "edge":
        return webdriver.Edge()
    else:
        raise ValueError("Unsupported browser!")

def automate_age_calculator(browser_name):
    driver = init_browser(browser_name)

        # Step 1: Open URL
    driver.get("https://www.easycalculation.com/")
    driver.maximize_window()
    time.sleep(2)

        # Step 2: Click on "Age Calculator"
    age_calculator_link = driver.find_element(By.LINK_TEXT, "Age Calculator")
    age_calculator_link.click()
    time.sleep(2)

        # Count number of links and images
    links = driver.find_elements(By.TAG_NAME, "a")
    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"Total Links: {len(links)}, Total Images: {len(images)}")

    # Print first 10 links
    print("\nFirst 10 Links:")
    for link in links[:10]:
        print(link.get_attribute("href"))

    # Print first 5 images
    print("\nFirst 5 Images:")
    for image in images[:5]:
        print(image.get_attribute("src"))

    # Step 3: Enter Date of Birth
    driver.find_element(By.NAME, "day").send_keys("31")
    driver.find_element(By.NAME, "month").send_keys("05")
    driver.find_element(By.NAME, "year").send_keys("1978")
    time.sleep(5)
    # Step 4: Click "GO" button
    driver.find_element(By.XPATH, "//*[@id='dispCalcConts']/div[3]/form/table/tbody/tr[10]/td/input[1]").click()
    time.sleep(5)

    # Step 5: Print results
    print("\nAge Calculation Results:")
    age = driver.find_element(By.ID, "result1").text
    age_in_days = driver.find_element(By.ID, "result2").text
    age_in_hours = driver.find_element(By.ID, "result3").text
    age_in_minutes = driver.find_element(By.ID, "result4").text

    print(f"Your Age is: {age}")
    print(f"Your Age in Days: {age_in_days}")
    print(f"Your Age in Hours: {age_in_hours}")
    print(f"Your Age in Minutes: {age_in_minutes}")

    # Step 6: Click Reset
    driver.find_element(By.XPATH, "//'dispCalcConts']/div[3]/form/table/tbody/tr[10]/td/input[2]").click()
    time.sleep(5)
    driver.quit()

# Automate for Chrome and Edge
print("Automating on Chrome...")
automate_age_calculator("chrome")

#print("Automating on Edge...")
#automate_age_calculator("edge")
