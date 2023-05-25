#儲存檔案
# file = open('data.txt',mode = 'w',encoding='utf8')
# file.write('測試中文\n好棒棒')
# file.close()

# with open ('data.txt',mode='w',encoding='utf8') as file:
#     file.write('5\n3')
#讀取檔案
# sum = 0
# with open ('data.txt',mode = 'r',encoding='utf8') as file:
#     for line in file:
#         sum+=int(line)
# print(sum)
#使用 JSON 格式讀取、複寫檔案
import json
with open('config.json',mode='r',encoding='big5') as file:
    data = json.load(file)
print(data) #data是一個字典
data['name']='New Name' #修改變數中的資料
# print('name:',data['name'])
# print('version:',data['version'])

#把最新的資料複寫回檔案中
with open('config.json',mode='w') as file:
    json.dump(data, file)