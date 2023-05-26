#抓取PTT八卦版的網頁原始碼 (HTML)
import urllib.request as req
def getData(url):

# url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
#建立一個Request物件，附加Request Headers的資訊
    request = req.Request(url, headers={
        'cookie':'over18=1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    #解析原始碼，取得每天文章的標題
    import bs4
    root = bs4.BeautifulSoup(data,'html.parser')
    # print(root.title.string)
    titles = root.find_all('div',class_='title') #尋找class='title的div標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)  #如果標題包含a標籤 (沒有被刪除) 印出來
    #抓取上一頁的連結
    nextLink = root.find('a',string='‹ 上頁') #找到內文是‹ 上頁的a 標籤
    return (nextLink['href'])

#主程序:抓取多個頁面的標題
pageURL = 'https://www.ptt.cc/bbs/Gossiping/index.html'
count = 0
while count <5:
    pageURL = 'https://www.ptt.cc'+getData(pageURL)
    count+=1