# # # 集合的運算
# # s1 = {3,4,5}
# # print( 10 not in s1)
# # s1 = {3,4,5}
# # s2 = {4,5,6,7}
# # # s3 = s1&s2 #交集 
# # # s3 = s1|s2 #聯集
# # # s3 = s1-s2 #差集
# # s3 = s1^s2 #反交集 取兩個集合中不重疊的部分
# # print(s3)
# # s = set('Hello') #set(字串)
# # print('H' in s)
# #字典的運算
# dic = {'apple':'蘋果','bug':'蟲蟲'}
# dic['apple'] = '小蘋果' #改變字典資料
# # print(dic['apple'])
# # print('apple' in dic) #判斷key是否存在
# print(dic)
# del dic['apple'] #刪除字典中的鍵值對
# print(dic)

dic = {x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)
