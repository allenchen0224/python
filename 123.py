
import requests as req

#目標網站
url = "https://www.ptt.cc/man/part-time/DF76/D780/DC4F/index.html"

#請求網站
r = req.get(url)

#檢查回應。如果是200則成功請求
print(r)
<Response [200]>
import bs4

#透過BeautiFul整理且用html.parser解析
root = bs4.BeautifulSoup(r.text,"html.parser")
#找到所有屬性class = "m-ent"
ment = root.find_all("div",class_="m-ent")
#一個一個印出要的資料
for title in ment:
    print(title.a.string)#取得文章標題
    print("https://www.ptt.cc"+title.a.get("href"))#取得文章連結