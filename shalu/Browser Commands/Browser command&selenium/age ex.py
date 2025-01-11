from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#step:1
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.easycalculation.com/index.php#google_vignette")
time.sleep(3)
#step:2
y = driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[6]/div[2]/div[1]/ul[1]/li[1]/a[1]").click()
time.sleep(2)

links = driver.find_elements(By.XPATH,".//a")
print(len(links))
print("First 10 links :")
for link in links[:10]:
    print(link.get_attribute("href"))

images = driver.find_elements(By.TAG_NAME, "img")
print(len(images))
print(f"First 5 image links:")
for img in images[:5]:
    print(img.get_attribute("src"))

driver.find_element(By.ID, "i21").send_keys("19")
driver.find_element(By.ID, "i22").send_keys("05")
driver.find_element(By.ID, "i23").send_keys("1999")

#Step:3
z = driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[6]/div[3]/form[1]/table[1]/tbody[1]/tr[10]/td[1]/input[1]").click()
time.sleep(3)

#Step:4
t1 = driver.find_element(By.ID,"r1")
print(f"Your age is:  {t1.get_attribute("value")}")
t2 = driver.find_element(By.ID,"r4")
print(f"Your age in days :  {t2.get_attribute("value")}")
t3 = driver.find_element(By.ID,"r3")
print(f"Your age in Hours :  {t3.get_attribute("value")}")
t4 = driver.find_element(By.ID,"r2")
print(f"Your age in Minutes :  {t4.get_attribute("value")}")

#Step:5
x = driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[6]/div[3]/form[1]/table[1]/tbody[1]/tr[10]/td[1]/input[2]").click()
time.sleep(3)