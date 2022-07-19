import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv("C:/Users/Administrator/Desktop\Machine-Learning-with-R-datasets-master/insurance.csv")
x = data.iloc[:,:-1]

y = data.iloc[:,-1]

x_obj = x.select_dtypes(include=["object"])



x_non_obj = x.select_dtypes(exclude=["object"])

la = LabelEncoder()
for i in range(x_obj.shape[1]):
    x_obj.iloc[:,i]= la.fit_transform(x_obj.iloc[:,i])

X = pd.concat([x_non_obj,x_obj],axis=1)    

x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=0.85)

m = LinearRegression()

m.fit(x_train,y_train)

print(m.score(x_train,y_train))

print(m.score(x_test,y_test))