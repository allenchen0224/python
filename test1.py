# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.options import Options
# # # import time
 
 
# # # options = Options()
# # # options.add_argument("--disable-notifications")
 
# # # chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
# # # chrome.get("https://www.facebook.com/")

# # import matplotlib.pyplot as plt
# # x = [4,5,10,4,3,11,14,6,10,12]
# # y = [21,19,24,17,16,25,24,22,21,21]

# # # plt.scatter(x,y)
# # # plt.show()

# # from sklearn.cluster import KMeans
# # data = list(zip(x,y))
# # inertias =[]

# # for i in range(1,11):
# #     kmeans = KMeans(n_clusters=i)
# #     kmeans.fit(data)
# #     inertias.append(kmeans.inertia_)

# # # plt.plot(range(1,11),inertias, marker='o')
# # # plt.title('Elbow method')
# # # plt.xlabel('Number of clusters')
# # # plt.ylabel('Interia')
# # # plt.show()

# # kmeans = KMeans(n_clusters=2)
# # kmeans.fit(data)
# # plt.scatter(x,y,c=kmeans.labels_)
# # plt.show()


import matplotlib.pyplot as plt
import numpy as np

# # plt.subplot(2,1,2) #(列,行,第幾個)

# # y = np.array([3,8,1,10])
# # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] 
# # plt.rcParams['axes.unicode_minus'] = False
# # plt.title('這是標題',loc='center')
# # plt.xlabel('這是Ｘ軸名稱')
# # plt.ylabel('這是Ｙ軸名稱')
# # plt.plot(y,marker='o',ls=':',color='r',linewidth='1')
# # plt.grid(axis='x',color='green')
# # plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='plasma')
# plt.colorbar()
# plt.show()
# import numpy as np
# import random
# a = np.random.randint(0,11,size=10)
# print(a)

#條形圖 bar直 barh橫
# x = ['apples','bananas']
# y =[400,350]

# plt.bar(x,y,width=0.1)
# plt.show()

#直方圖 hist
# x = np.random.normal(170,10,250)
# plt.hist(x,color='red',width=0.8)
# plt.show()

y = np.array([35,25,25,15])
a = ['apple','banana','cherries','watermeleon']
b = [0.3,0.2,0,0]
plt.pie(y,labels=a,startangle=90,explode=b,shadow=True,autopct='%.1f%%') #startangle起始角度 explode 拉開多少 shadow 陰影
plt.legend(title='Four Fruits:',loc = 'lower right') #圖例 
plt.show()