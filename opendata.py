#網路連線
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as request
src = "https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data = response.read().decode('utf-8')
print(data) 
#串接、擷取公開資料
