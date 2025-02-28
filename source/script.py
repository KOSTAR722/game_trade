import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import time
import info
from twocaptcha import TwoCaptcha





def main(chrome_profile_path,mode,data=[""]):
    # プロファイルのディレクトリ（Windowsの場合）
    #chrome_profile_path = r'C:/Users/tonos/AppData/Local/Google/Chrome/User Data'

    # 使用するプロファイル名（例: "Profile 1"）
    profile_name = "Profile 1"

    options = Options()
    options.add_argument(f"--user-data-dir={chrome_profile_path}")
    options.add_argument(f"--profile-directory={profile_name}")

    solver = TwoCaptcha(info.Captha_API)  # 自分のAPIキーを設定してください

    #driver=selenium.webdriver.Chrome(options=options)
    driver=selenium.webdriver.Chrome(options=options)

    for datum in data:

        try:
            if mode=="手動" and datum[0]==False:
                continue
                
            driver.get("https://maclub.jp/mypage")
            time.sleep(5)
            driver.find_element(By.XPATH,'//*[@id="content-wrapper"]/a').click()
            time.sleep(3)
            driver.find_element(By.XPATH,'//*[@id="btn-search-title"]').click()

            time.sleep(3)
            driver.find_element(By.XPATH,'//*[@id="item-images"]').send_keys(datum[2])
            driver.find_element(By.XPATH,'//*[@id="search-title-input"]').send_keys(datum[3])
            time.sleep(3)
            select_genre=driver.find_element(By.XPATH,'//*[@id="search-title-container"]').find_elements(By.CLASS_NAME,"syllabary-list")
            time.sleep(3)
            print(len(select_genre))
            for list in select_genre:
                items=list.find_elements(By.TAG_NAME,"div")
                for item in items:
                    data_item=item.get_attribute("data-item")
                    print(data_item)
                    time.sleep(0.5)
                    if  (datum[3] in data_item) and (datum[4] in data_item):
                        item.click()
                        break

            time.sleep(3)

            driver.find_element(By.ID,'account-type-id-40').click()

            time.sleep(3)

            driver.find_element(By.ID,'name').send_keys(datum[5])
            time.sleep(3)
            driver.find_element(By.ID,'input-body-text').send_keys(datum[6])
            time.sleep(3)

            #買主へ初回自動表示するメッセージ
            driver.find_element(By.XPATH,'//*[@id="firstchat"]').send_keys(datum[7])
            time.sleep(3)

            #売却価格
            driver.find_element(By.XPATH,'//*[@id="price-block"]/div/div/div/div[1]/div[2]/div/input').send_keys(datum[8])
            time.sleep(3)

        except Exception as e:
            print("ミスったみたい")    
            print(e)



if __name__ == '__main__':
    main()
      
