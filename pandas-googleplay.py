import pandas as pd
data = pd.read_csv('googleplaystore.csv')
#觀察資料
# print('資料數量',data.shape)
# print('資料欄位',data.columns)
# print('============')
#分析資料：評分的各種統計數據
# data = data[(0<data['Rating']) & (data['Rating'] <=5)]
# condition = 
# data = data[condition]
# print(condition)
# print('平均數',data['Rating'].mean())
# print('中位數',data['Rating'].median())
# print('取得前一百個應用程式的平均',data['Rating'].nlargest(100).mean())

#分析資料：安裝數量的各種統計數據
# data['Installs'] = pd.to_numeric(data['Installs'].str.replace(",","").replace("Free","").str.replace("+",""))
# print('平均數',data['Installs'].mean())
# condition = data['Installs']>100000
# print('安裝數量大於100000的應用有幾個',data[condition].shape[0])

#基於資料的應用：關鍵字搜尋應用程式名稱
keyword = input('請輸入關鍵字：')
condition = data['App'].str.contains(keyword,case=False)
print('包含關鍵字的應用程式數量',data[condition]['App'].shape[0])