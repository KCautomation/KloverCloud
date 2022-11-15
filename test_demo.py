from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("C:\\Users\\shabr\\Downloads\\chromedriver_win32\\chromedriver.exe")

st1 = time.time()
driver.get("https://eks.alpha.klovercloud.io/")
driver.implicitly_wait(20)
time.sleep(2)
# driver.refresh()
