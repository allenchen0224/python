import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.ptt.cc/bbs/Gossiping/M.1685090290.A.66D.html',headers={'cookie':'over18=1'})
bs = BeautifulSoup(html.text, 'html.parser')
data = bs.find_all('div',class_ = 'bbs-screen bbs-content')
for i in data:
    print(i.text)
