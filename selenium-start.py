#載入Selenium 相關模組
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# #設定 Chrome Driver 的執行路徑
# options = Options()
# options.chrome_executable_path = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://google.com/')
time.sleep(5)
driver.close()