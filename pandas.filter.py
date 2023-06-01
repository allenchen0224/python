import pandas as pd

# data = pd.Series([30,15,20])
# condition = data >18
# print(condition)
# filterData = data[condition]
# print(filterData)

# data = pd.Series(['您好','Python','Pandas'])
# condition = data.str.contains('P')
# print(condition)
# filterData = data[condition]
# print(filterData)

#篩選練習
data = pd.DataFrame({'name':['Amy','Bob','Charles'],'salary':[30000,50000,40000]})
print(data)
condition = data['name']=='Amy'
print(condition)
a = data[condition]
print(a)