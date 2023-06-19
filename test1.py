# # # # from selenium import webdriver
# # # # from selenium.webdriver.chrome.options import Options
# # # # import time
 
 
# # # # options = Options()
# # # # options.add_argument("--disable-notifications")
 
# # # # chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
# # # # chrome.get("https://www.facebook.com/")

# # # import matplotlib.pyplot as plt
# # # x = [4,5,10,4,3,11,14,6,10,12]
# # # y = [21,19,24,17,16,25,24,22,21,21]

# # # # plt.scatter(x,y)
# # # # plt.show()

# # # from sklearn.cluster import KMeans
# # # data = list(zip(x,y))
# # # inertias =[]

# # # for i in range(1,11):
# # #     kmeans = KMeans(n_clusters=i)
# # #     kmeans.fit(data)
# # #     inertias.append(kmeans.inertia_)

# # # # plt.plot(range(1,11),inertias, marker='o')
# # # # plt.title('Elbow method')
# # # # plt.xlabel('Number of clusters')
# # # # plt.ylabel('Interia')
# # # # plt.show()

# # # kmeans = KMeans(n_clusters=2)
# # # kmeans.fit(data)
# # # plt.scatter(x,y,c=kmeans.labels_)
# # # plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # # plt.subplot(2,1,2) #(列,行,第幾個)

# # # y = np.array([3,8,1,10])
# # # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] 
# # # plt.rcParams['axes.unicode_minus'] = False
# # # plt.title('這是標題',loc='center')
# # # plt.xlabel('這是Ｘ軸名稱')
# # # plt.ylabel('這是Ｙ軸名稱')
# # # plt.plot(y,marker='o',ls=':',color='r',linewidth='1')
# # # plt.grid(axis='x',color='green')
# # # plt.show()

# # x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# # y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# # colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
# # sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# # plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='plasma')
# # plt.colorbar()
# # plt.show()
# # import numpy as np
# # import random
# # a = np.random.randint(0,11,size=10)
# # print(a)

# #條形圖 bar直 barh橫
# # x = ['apples','bananas']
# # y =[400,350]

# # plt.bar(x,y,width=0.1)
# # plt.show()

# #直方圖 hist
# # x = np.random.normal(170,10,250)
# # plt.hist(x,color='red',width=0.8)
# # plt.show()

# # y = np.array([35,25,25,15])
# # a = ['apple','banana','cherries','watermeleon']
# # b = [0.3,0.2,0,0]
# # plt.pie(y,labels=a,startangle=90,explode=b,shadow=True,autopct='%.1f%%') #startangle起始角度 explode 拉開多少 shadow 陰影
# # plt.legend(title='Four Fruits:',loc = 'lower right') #圖例 
# # plt.show()

# # import statistics
# # a = [1,2,3,4,4,4,5,6,7,8,8,8,8,8,8]

# # x = statistics.mode(a) #眾數
# # y = statistics.stdev(a) #標準差
# # z = statistics.variance(a) #變異數
# # print(x)
# # print(y)
# # print(z)

# # x= 'awesome'
# # def myfunc():
# #     print('Python is '+x)
# # myfunc()

# # print('Python is '+x)

# # def myfunc():
# #     global x
# #     x = 'fantastic'
# # myfunc()

# # print('Python is '+x)

# # a = 'hello'
# # # print(txt.lower())
# # b = 'world'
# # # b = a.strip()
# # print(a+' '+b)

# # import random 
# # num = random.randint(1,3)
# # answer = eval(input('請猜數字1~3:'))
# # while num != answer:
# #     answer = eval(input('請猜數字1~3:'))
# #     print(num ,'==',answer,'is',num==answer)


# # def cal(x,y):
# #     div = x//y
# #     mod = x%y
# #     return div,mod
# # a,b = cal(120,7)
# # print('120除7的傷數為:',a,'餘數為:',b)

# # x = np.random.uniform(0.0,5.0,10000)

# # plt.hist(x,10) #(幾條柱)
# # plt.show()

# s = 'MCMXCIV'
# a = 0
# # if (s[0]=='M') & (s[1]=='M') & (s[2]=='M'):
# #     a += 3000
# # elif (s[0]=='M') & (s[1]=='M'):
# #     a += 2000
# # elif s[0] =='M':
# #     a += 1000

# # for i in range(len(s)):
# #     if s[i] =='M':
# #         a +=1000
# #     elif s[i] != 'M':
# #         break
    
# # for j in range(len(s)):
# #     if s[j] != 'M' and s[j] !='D' and s[j] !='C':
# #         break
# #     elif s[j] =='D':
# #         a+=500
# #     elif s[j-1] =='C' and s[j]=='M':
# #         a+=900
# #     elif s[j-1] =='C' and s[j] =='D':
# #         a+=400
# #     elif s[j-1] =='C' and s[j] !='M':
# #         a+=100

# # for k in range(len(s)):
# #     if s[k] != 'M' and s[k] !='D' and s[k] !='C' and s[k] !='X' and s[k] !='L':
# #         break
# #     elif s[k-1] =='X' and s[k] =='C':
# #         a +=90
# #     elif s[k-1] =='X' and s[k] =='L':
# #         a +=40
# #     elif s[k] =='L':
# #         a +=50
# #     elif s[k-1] =='X' and s[k] !='C':
# #         a+=10

# # for l in range(len(s)):
# #     if s[l-1] =='I' and s[l] =='X':
# #         a+=9
# #     elif s[l-1] =='I' and s[l] =='V':
# #         a+=4
# #     elif s[l-1] !='I' and s[l] =='V':
# #         a+=5
# #     elif s[l-1] =='I':
# #          a+=1
# # # if s[-1] =='I':
# # #     a+=1
# # # elif s[-1] =='V':
# # #     a+=5
# # # elif s[-1] =='X':
# # #     a+=5
# # # elif s[-1] =='L':
# # #     a+=5
# # # elif s[-1] =='C':
# # #     a+=5
# # # elif s[-1] =='D':
# # #     a+=500

# # print(a)

# import pandas as pd
# ss1 = pd.Series([4,7,-5,3], index = ['a','b','c','d'])

# print(ss1.index)
# print(ss1['a'])
# print('a' in ss1)
# print(7 in ss1)
# print(7 in ss1.values)

from numpy import random
x = random.normal(0,10,size=(2,3))
print(x)