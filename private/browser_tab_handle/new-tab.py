
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from urllib.request import urlopen
from urllib.error import *


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(3)
# open new tab
driver.execute_script("window.open('https://twitter.com')")
time.sleep(3)
print (driver.current_window_handle)

# Switch to new window
driver.switch_to.window(driver.window_handles[-1])
time.sleep(4)
print (" Twitter window should go to facebook ")
print ("New window ", driver.title)
driver.get("http://facebook.com")
time.sleep(2)
print ("New window ", driver.title)

# Switch to old window
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
print (" Linkedin should go to gmail ")
print ("Old window ", driver.title)

driver.get("http://gmail.com")
print ("Old window ", driver.title)
time.sleep(2)

# Again new window
driver.switch_to.window(driver.window_handles[1])
print (" Facebook window should go to Google ")
time.sleep(2)
print ("New window ", driver.title)
driver.get("http://google.com")
time.sleep(2)
print ("New window ", driver.title)
time.sleep(2)
