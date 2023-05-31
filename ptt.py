import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
html = requests.get('https://www.ptt.cc/bbs/hotboards.html')
soup = BeautifulSoup(html.text,'html.parser')
list = []
a = soup.find_all('div',class_='board-name')
for i in a:
    list.append(i.text)

b= input('請輸入欲查詢的分類：')
if b in list:
    b = b
else:
    b = input('請重新輸入欲查詢的分類：')
    
r = requests.get('https://www.ptt.cc/bbs/'+b+'/index.html',headers={'cookie':'over18=1'})
soup1 = BeautifulSoup(r.text,'html.parser')
btn = soup1.select('div.btn-group >a')
next_page = btn[3]['href']
new = int(btn[3]['href'].split("index")[-1].split(".html")[0].strip())+1

n = eval(input('請輸入欲查詢的頁數:'))
end = new-n
c=[]
d=[]
def search(content):
    for page in range(new,end,-1):
        content = requests.get('https://www.ptt.cc/bbs/'+b+'/index'+str(page)+'.html',headers={'cookie':'over18=1'})
    
        soup = BeautifulSoup(content.text,'html.parser')
        title = soup.find_all('div',class_='title')
        for i in title:
            c.append(i.text.strip('\n'))
        print(c)
        link = soup.find_all('div',class_='title')
        for j in link:
            if j.select_one('a').get('href') != '':
                d.append('https://www.ptt.cc/'+j.select_one("a").get("href"))
            else:
                d.append('')
        print(d)
search('content')

dict1 = {'title':c,'link':d}
df = pd.DataFrame(dict1)
df.to_csv('ppt.csv',encoding='utf-8-sig',index = False)
