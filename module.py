#載入內建的sys模組並取得資訊
# import sys
# print(sys.platform)
# print(sys.maxsize)

#建立geometry模組,載入使用
# import geometry
# result = geometry.distance(0,0,3,4)
# print(result)

#調整搜尋模組的路徑
# import sys
# print(sys.path) #印出模組的搜尋路徑
from modules import geometry
print(geometry.distance(0,0,3,4))