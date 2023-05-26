import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.ptt.cc/bbs/Gossiping/M.1685090290.A.66D.html',headers={'cookie':'over18=1'})
bs = BeautifulSoup(html.text, 'html.parser')
data = bs.find('div',class_ = 'article-metaline')
# for i in data:
#     print(i.text)
previous = data.find_previous_siblings('div')
print(previous)