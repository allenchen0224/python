# s = [1,5,9,3,7]
# for i in range(len(s)-1):
#     for j in range(len(s)-1-i):
#         if s[j] > s[j+1]:
#             s[j],s[j+1]=s[j+1],s[j]
# print(s)
# dic = {'a':'3','x':'10'}

#iterable 資料型態
# for key in dic:
#     print(key)
#     print(dic[key])

#內建函式
#max(可迭代資料)
#sorted(可迭代資料)
# result = max([10,2,30,1])
# print(result)
# result = max('xaz')
# print(result)
# result = max({10,200,30,1})
# print(result)
# result = max({'x':3,'a':4})
# print(result)

#sorted(可迭代資料)
result = sorted('cba')
print(result)
result = sorted({10,2,100,-5})
print(result)
result = sorted({'b':3,'a':4})
print(result)