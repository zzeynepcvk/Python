from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Edge()


url = "https://www.gazetepusula.net"

driver.get(url)