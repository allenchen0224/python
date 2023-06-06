# # import numpy as np
# # import matplotlib.pyplot as plt

# # t = np.arange(-6,6,0.1)
# # s = 1/(1+(np.e**(-t)))
# # plt.plot(t,s)
# # plt.title('sigmoid function')
# # plt.show()

# import pandas as pd
# import numpy as np
# from sklearn import preprocessing,linear_model

# train_data = pd.read_csv('train.csv')
# train_data.info()

# age_median = np.nanmedian(train_data['Age'])
# print()
# print('年齡中位數',age_median)
# print()
# new_age = np.where(train_data['Age'].isnull(),age_median,train_data['Age'])
# train_data['Age'] = new_age

# train_data.info()

# label_encoder = preprocessing.LabelEncoder()
# encoded_class = label_encoder.fit_transform(train_data['Pclass'])
# encoded_Sex = label_encoder.fit_transform(train_data["Sex"])

# x = pd.DataFrame([encoded_class,encoded_Sex,train_data['Age']]).T
# y = train_data['Survived']

# logisitic = linear_model.LogisticRegression()
# logisitic.fit(x,y)

# # print('迴歸係數:',logisitic.coef_)
# # print('截距:',logisitic.intercept_)

# print('混淆矩陣')
# preds = logisitic.predict(x)
# print(pd.crosstab(train_data['Survived'],preds))
# print((454+248)/(454+248+94+95))
# print(logisitic.score(x,y))

# from sklearn import datasets
# iris = datasets.load_iris()
# print(iris.keys())

# print(iris.data.shape)
# print(iris.feature_names)
# print(iris.DESCR)

# import pandas as pd
# from sklearn import datasets
# from sklearn import tree
# from sklearn.model_selection import train_test_split

# iris = datasets.load_iris()
# x = pd.DataFrame(iris.data,columns=iris.feature_names)
# target = pd.DataFrame(iris.target, columns=['target'])
# y = target['target']

# xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.33,random_state=1)
# dtree = tree.DecisionTreeClassifier(max_depth=3)
# dtree.fit(xtrain,ytrain)

# print('準確率:',dtree.score(xtest,ytest))

# print(dtree.predict(xtest))
# print(ytest.values)

import pandas as pd
import numpy as np
from sklearn import neighbors

x = pd.DataFrame({'durability':[7,7,3,1],'strength':[7,7,4,4]})
y = np.array([0,0,1,1])
k =3
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(x,y)

new = pd.DataFrame(np.array([[3,7]                                                                   cdcxzx?/--A/]))
pred = knn.predict(new)
print(pred)