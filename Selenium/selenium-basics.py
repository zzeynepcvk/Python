from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
#driver.save_screenshot("github-ss.png")

url = "http://github.com/zzeynepcvk"
driver.get(url)

print(driver.title)

if "zzeynepcvk" in driver.title:
    driver.save_screenshot("github-zeynep.png")

time.sleep(2)

driver.back()
time.sleep(2)

driver.close()


