import datetime
import csv
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
driver = webdriver.Chrome(options=options)
# driver.maximize_window() 網頁最大化

driver.get('https://kma.kkbox.com/charts/yearly/newrelease?lang=tc&terr=tw')

artist = []
song = []
issued_date = []
rank = []

n = 0 
while n <1:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') #捲動視窗到底部
    time.sleep(5)
    n+=1


a = driver.find_elements(By.CLASS_NAME, "charts-list-rank")
b = driver.find_elements(By.CSS_SELECTOR, '[class=charts-list-song]')
c = driver.find_elements(By.CSS_SELECTOR, '[class=charts-list-artist]')
d = driver.find_elements(By.CSS_SELECTOR, '[class=charts-list-date]')

for i in a:
    if i.text == '當日':
        continue
    rank.append(i.text)

for j in b:
    if j.text == '':
        continue
    song.append(j.text)

for k in c:
    if k.text == '':
        continue
    artist.append(k.text)

for l in d:
    if l.text == '':
        continue
    issued_date.append(l.text)

current_date = datetime.datetime.now().strftime('%Y%m%d')

dict1 = {'rank':rank,'song':song,'artist':artist,'issued_date':issued_date}
df = pd.DataFrame(dict1)
df.to_csv(current_date+'kkbox.csv',encoding='utf-8-sig',index = False)



