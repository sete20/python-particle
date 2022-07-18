import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


x = np.array([ 1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,19,20])
y = np.array([10,20,30,40,50,60,70,80,90,100,110,120,150,160,170,180,190,200])


x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m =LinearRegression()
m.fit(x_train.reshape(1, -1)
,y_train.reshape(1, -1)
)

print(m.score(x_test.reshape(1, -1),x_test.reshape(1, -1)))
plt.scatter(x_train,y_train)
plt.plot(x_train.reshape(1, -1),m.predict(x_train.reshape(1, -1)),color="red")
plt.show()
# print(x_train)
# print(y_train)
