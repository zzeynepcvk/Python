from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://youtube.com"

driver.get(url)

searchInput = driver.find_element(By.NAME, 'search_query')


time.sleep(1)

searchInput.send_keys("zeynepcevik722")
time.sleep(1)


searchInput.send_keys(Keys.ENTER)
time.sleep(4)

result = driver.find_elements(By.CSS_SELECTOR, '#content a')

""" result = driver.page_source
print(result) """

driver.save_screenshot("basardim-zey.png")
time.sleep(2)

for element in result:
    print(element.text)


driver.close()

