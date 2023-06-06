import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#一維資料 線性迴歸
# temperatures = np.array([29,28,34,31,25,29,32,
#                          31,24,33,25,31,26,30])
# drink_sales = np.array([7.7,6.2,9.3,8.4,5.9,6.4,8.0,
#                         7.5,5.8,9.1,5.1,7.3,6.5,8.4])
# x = pd.DataFrame(temperatures, columns=['Temperature'])
# y = pd.DataFrame(drink_sales, columns=['Drink_Sales'])

# lm = LinearRegression()
# lm.fit(x,y)
# print('迴歸係數：',lm.coef_)
# print('截距：',lm.intercept_)

# new = pd.DataFrame(np.array([26,30]),columns=['Temperature'])
# predicted_sales = lm.predict(new)
# print(predicted_sales)

# plt.scatter(temperatures,drink_sales,color='red')
# regression_sales = lm.predict(x)
# plt.plot(temperatures,regression_sales,color='black')
# plt.plot(new,predicted_sales,color='blue',marker='o',markersize=10)
# plt.show()

##
#二維資料 線性迴歸
# waist_heights = np.array([[67,160],[68,165],[70,167],[65,170],[80,165],[85,167],[78,178],[79,182],[95,175],[89,172]])
# weights = np.array([50,60,65,65,70,75,80,85,90,81])
# x = pd.DataFrame(waist_heights,columns=['Waist','Height'])
# y = pd.DataFrame(weights,columns=['Weight'])
# lm = LinearRegression()
# lm.fit(x,y)
# print('迴歸係數:',lm.coef_)
# print('截距:',lm.intercept_)

# new = pd.DataFrame(np.array([[66,164],[82,172]]))
# predicted_weights = lm.predict(new)
# print(predicted_weights)

# from sklearn import datasets
# # boston = datasets.load_boston()
# # print(boston.keys())
# diabetes = datasets.load_diabetes()
# print(diabetes.keys())

# x = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
# print(x.head())

import random
# for i in range(5):
#     print(random.randint(1,100))

random.seed(101)
for i in range(5):
    print(random.randint(1,100))