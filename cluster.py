# import pandas as pd
# import numpy as np
# from sklearn import cluster
# import matplotlib.pyplot as plt

# df =pd.DataFrame({'length':[51,46,51,45,51,50,33,38,37,33,33,21,23,24],'weight':[10.2,8.8,8.1,7.7,9.8,7.2,4.8,4.6,3.5,3.3,4.3,2.0,1.0,2.0]})

# k = 3

# kmeans = cluster.KMeans(n_clusters=k,random_state=12)
# kmeans.fit(df)
# print(kmeans.labels_)

# colmap = np.array(['r','g','y'])
# plt.scatter(df['length'],df['weight'],color = colmap[kmeans.labels_])
# plt.show()


# import pandas as pd
# import numpy as np
# from sklearn import datasets
# from sklearn import cluster
# import matplotlib.pyplot as plt

# iris = datasets.load_iris()

# x = pd.DataFrame(iris.data,columns=iris.feature_names)
# x.columns = ['sepal_length','sepal_width','petal_length','petal_width']
# y = iris.target
# k = 3

# kmeans = cluster.KMeans(n_clusters=k,random_state=12)
# kmeans.fit(x)
# print(kmeans.labels_)
# print(y)

# colmap = np.array(['r','g','y'])
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.scatter(x['petal_length'],x['petal_width'],color =colmap[y])
# plt.xlabel('Petal Length')
# plt.ylabel('Petal Width')
# plt.title('Real Classification')
# plt.subplot(1,2,2)
# plt.scatter(x['petal_length'],x['petal_width'],color =colmap[kmeans.labels_])
# plt.xlabel('Petal Length')
# plt.ylabel('Petal Width')
# plt.title('K-means Classification')
# plt.show()

# kmeans = cluster.KMeans(n_clusters=k,random_state=12)
# kmeans.fit(x)
# print('K-means Classification')
# print(kmeans.labels_)

# #修正標籤錯誤
# pred_y = np.choose(kmeans.labels_,[2,0,1]).astype(np.int64)
# print('K-means Fix Classification')
# print(pred_y)
# print('Real Classification')
# print(y)

# import sklearn.metrics as sm
# # kmeans = cluster.KMeans(n_clusters=k,random_state=12)
# # kmeans.fit(x)
# # pred_y = np.choose(kmeans.labels_,[2,0,1]).astype(np.int64)
# print(sm.accuracy_score(y,pred_y)) #績效矩陣 (準確率)
# print(sm.confusion_matrix(y,pred_y)) #混淆矩陣 (斜線/全部)＝準確率

# import matplotlib.pyplot as plt
# from sklearn.datasets import make_blobs
# from sklearn.cluster import KMeans

# dx,dy = make_blobs(n_samples=500,n_features=2,centers=10,random_state=42)
# kmeans = KMeans(n_clusters=5)
# kmeans.fit(dx)

# new_dy = kmeans.predict(dx)
# plt.rcParams['font.size'] = 14
# plt.figure(figsize=(16,8))

# plt.subplot(1,2,1)
# plt.title('Original data(5 groups)')
# plt.scatter(dx.T[0],dx.T[1],c=dy,cmap=plt.cm.Set1)

# plt.subplot(1,2,2)
# plt.title('KMeans=5 groups')
# plt.scatter(dx.T[0],dx.T[1],c=new_dy,cmap=plt.cm.Set1)

# plt.tight_layout()
# plt.show()

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Safari()
# sleep(3)
# driver.quit

# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
service = Service('/Users/chenweihao/Documents/python/chromedriver')  
# default location /usr/local/bin 
driver = webdriver.Chrome(service=service) # service=service)
sleep(3)
driver.quit