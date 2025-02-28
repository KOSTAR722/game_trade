from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_argument('--user-data-dir=C:\\Users\\tonos\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Default')
options.add_argument('--lang=en')
driver = webdriver.Chrome(options=options)
driver.get("chrome://version")
time.sleep(1000)
#driver.quit()