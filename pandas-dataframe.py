#載入Pandas模組
import pandas as pd
#資料索引：pd.Dataframe(字典,index=索引列表)
data = pd.DataFrame({'name':['Amy','Bob','Charles'],'salary':[30000,50000,40000]},index = ['a','b','c'])
# print(data)
# print('=========')
#觀察資料
# print('資料數列',data.size)
# print('資料形狀(列,蘭)',data.shape)
# print('資料索引',data.index)

# print('取得第二列',data.iloc[1],sep='\n')
# print('=======')
# print('取得第三列',data.loc['c'],sep='\n')

#取得蘭的Ｓeries資料
# print('取得name欄位',data['name'],sep='\n')
# names = data['name']
# print('把name全部大寫',names.str.upper(),sep='\n')

# #計算薪水的平均值
# salaries = data['salary']
# print('薪水的平均值',salaries.median())

#建立新的欄位
data['revenue'] = [500000,400000,300000]
data['rank'] = pd.Series([3,6,1],index = ['a','b','c'])
data['cp'] = data['revenue']/data['salary']
print(data)