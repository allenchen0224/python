import requests
from bs4 import BeautifulSoup
html = requests.get('https://www.ptt.cc/bbs/hotboards.html')
soup = BeautifulSoup(html.text,'html.parser')
list = []
a = soup.find_all('div',class_='board-name')
for i in a:
    list.append(i.text)
# print(list)
# https://www.ptt.cc/bbs/Gossiping/index.html
# https://www.ptt.cc/bbs/hotboards.html

b= input('請輸入欲查詢的分類：')
if b in list:
    b = b
else:
    b = input('請重新輸入欲查詢的分類：')

c=[]
d=[]
def search(content):
    content = requests.get('https://www.ptt.cc/bbs/'+b+'/index.html',headers={'cookie':'over18=1'})

    soup = BeautifulSoup(content.text,'html.parser')
    # ment = soup.find_all("div",class_="m-ent")
    # #一個一個印出要的資料
    # for title in ment:
    #     print(title.a.string)#取得文章標題
    #     print("https://www.ptt.cc"+title.a.get("href"))#取得文章連結
    title = soup.find_all('div',class_='title')
    for i in title:
        c.append(i.text.strip('\n'))
    print(c)
    link = soup.find_all('div',class_='title')
    for j in link:
        d.append('https://www.ptt.cc/'+j.select_one("a").get("href"))
    print(d)

def more(content):
    content = requests.get('https://www.ptt.cc/bbs/'+b+'/index'+url+'.html',headers={'cookie':'over18=1'})

    soup = BeautifulSoup(content.text,'html.parser')
    # ment = soup.find_all("div",class_="m-ent")
    # #一個一個印出要的資料
    # for title in ment:
    #     print(title.a.string)#取得文章標題
    #     print("https://www.ptt.cc"+title.a.get("href"))#取得文章連結
    title = soup.find_all('div',class_='title')
    for i in title:
        c.append(i.text.strip('\n'))
    print(c)
    link = soup.find_all('div',class_='title')
    for j in link:
        d.append('https://www.ptt.cc/'+j.select_one("a").get("href"))
    print(d)

n = eval(input('請輸入欲查詢的頁數:'))
for page in range(1,n+1):
    r = requests.get('https://www.ptt.cc/bbs/'+b+'/index.html',headers={'cookie':'over18=1'})
    soup = BeautifulSoup(r.text,'html.parser')
    btn = soup.select('div.btn-group >a')
    next_page = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + next_page
    url = next_page_url
    if page ==1:
        search('content')
    else:
        more('content')

    # btn = soup.select('div.btn-group > a')
    # up_page_href = btn[3]['href']
    # next_page_url = 'https://www.ptt.cc' + up_page_href
    # url = next_page_url
    # search('content')