#載入pandas模組
import pandas as pd

# 建立Series
# data = pd.Series([20,10,15])
# # 基本Series操作
# print(data.max())
# print(data.median())
# data ==20
# print(data)
#建立DataFrame
data = pd.DataFrame({'name':['Amy','John','Bob'],'salary':[30000,50000,40000]})
#基本DataFrame操作
# print(data)
# print(data['salary'])
print(data)
print('==========')
print(data.iloc[1]) #印出第二列