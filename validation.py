from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = './chromedriver'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

LOGIN_PAGE = "https://www.seekingalpha.com/login"
ACCOUNT = "account.com"
PASSWORD = "password"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

driver.get("https://www.seekingalpha.com/login")
username = driver.find_element(By.NAME, "email")
username.send_keys(ACCOUNT)
password = driver.find_element(By.NAME, "password")
password.send_keys(PASSWORD)

submit_button = driver.find_element(By.CSS_SELECTOR,
                                    "button._60b46-2mbi1 _60b46-2LbhQ _60b46-1HfKK _60b46-qZydf _60b46-1uOHx _60b46-2NDcV _60b46-3YvwX _60b46-22lGb _60b46-1qE-_ _60b46-3DOuR _60b46-1UPRS _12b23-2JWwg _60b46-EQJB_")
submit_button.click()

driver.get(
    "https://seekingalpha.com/article/4414043-agenus-inc-agen-ceo-garo-armen-on-q4-2020-results-earnings-call-transcript")
text_element = driver.find_element(By.XPATH, '//*')

text = text_element

for t in text:
    print(t.text)
