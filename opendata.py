#網路連線
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# import urllib.request as request
# src = "https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data = response.read().decode('utf-8')
# print(data) 
#串接、擷取公開資料
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as request
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)
#將公司名稱列表出來
clist = data['result']['results']
# for company in clist:
#     print(company['公司名稱'],company['公司地址'])

with open('data.txt','w',encoding='utf-8') as file:
    for company in clist:
        file.write(company['公司名稱']+' 地址:'+company['公司地址']+'\n')