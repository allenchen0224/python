import requests
from bs4 import BeautifulSoup
url="https://www.ptt.cc/bbs/Food/index.html"
# goal = input('請輸入：')
# url= 'https://www.ptt.cc/bbs/Gossiping/search?q='+goal
def get_all_href(url):
    r = requests.get(url,headers={'cookie':'over18=1'})
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.select("div.title")
    for item in results:
        a_item = item.select_one("a")
        title = item.text
        if a_item:
            print(title, 'https://www.ptt.cc'+ a_item.get('href'))
        
for page in range(1,4):
    r = requests.get(url,headers={'cookie':'over18=1'})
    soup = BeautifulSoup(r.text,"html.parser")
    btn = soup.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url = next_page_url
    get_all_href(url = url)


# import requests 
# # 導入 BeautifulSoup 模組(module)：解析HTML 語法工具
# import bs4

# def crawler(URL):
#     # 文章連結
#     # URL = "https://www.ptt.cc/bbs/Gossiping/M.1685431400.A.42C.html"
#     # 設定Header與Cookie
#     my_headers = {'cookie': 'over18=1;'}
#     # 發送get 請求 到 ptt 八卦版
#     response = requests.get(URL, headers = my_headers)


#     #  把網頁程式碼(HTML) 丟入 bs4模組分析
#     soup = bs4.BeautifulSoup(response.text,"html.parser")

#     ## PTT 上方4個欄位
#     header = soup.find_all('span','article-meta-value')

#     # 作者
#     author = header[0].text
#     # 看版
#     board = header[1].text
#     # 標題
#     title = header[2].text
#     # 日期
#     date = header[3].text


#     ## 查找所有html 元素 抓出內容
#     main_container = soup.find(id='main-container')
#     # 把所有文字都抓出來
#     all_text = main_container.text
#     # 把整個內容切割透過 "-- " 切割成2個陣列
#     pre_text = all_text.split('--')[0]

#     # 把每段文字 根據 '\n' 切開
#     texts = pre_text.split('\n')
#     # 如果你爬多篇你會發現 
#     contents = texts[2:]
#     # 內容
#     content = '\n'.join(contents)


#     # 顯示
#     print('作者：'+author)
#     print('看板：'+board)
#     print('標題：'+title)
#     print('日期：'+date)
#     print('內容：'+content)

# crawler('https://www.ptt.cc/bbs/Gossiping/M.1685265873.A.D8B.html')