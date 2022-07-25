import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
#data = pd.read_csv("C:/Users/Administrator/Desktop/datasets/Iris.csv")
#print(data.isnull().sum())
data = pd.read_csv("C:/Users/Administrator/Desktop/datasets/stores.csv")
x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size= 0.95)
#model = DecisionTreeClassifier(max_depth=5).fit(x_train,y_train)

model = DecisionTreeRegressor(max_depth=5).fit(x_train,y_train)
print(model.score(x_train,y_train))
