from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import json

# プロファイルのディレクトリ（Windowsの場合）
chrome_profile_path = r'C:/Users/tonos/AppData/Local/Google/Chrome/User Data'

# 使用するプロファイル名（例: "Profile 1"）
profile_name = "Profile 1"

options = Options()
options.add_argument(f"--user-data-dir={chrome_profile_path}")
options.add_argument(f"--profile-directory={profile_name}")


driver=webdriver.Chrome(options=options)
# ChromeのWebDriverを起動

# 対象のページを開く（例：Google）
driver.get("https://maclub.jp/mypage")

# Cookieを取得
cookies = driver.get_cookies()

# CookieをJSONファイルに保存
with open("cookies.json", "w") as file:
    json.dump(cookies, file)

driver.quit()
