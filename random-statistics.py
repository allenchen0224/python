#隨機模組
import random
#隨機選取
# data = random.sample([1,5,6,10,20],3)
# print(data)
#隨機調換順序
# data = [1,5,8,20]
# random.shuffle(data)
# print(data)
#隨機取得亂數
# data = random.random()
# data = random.uniform(0.0,1.0) #0.0~1.0之間的隨機亂數
# print(data)
#取得常態分配亂數
#平均數100 標準差10
# data = random.normalvariate(100,10)
# print(data)

#統計模組
import statistics as stat
data= stat.stdev([1,2,3,4,5,8,10])
print(data)