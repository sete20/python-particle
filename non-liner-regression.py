import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import csv
data = pd.read_csv(
    "C:/Users/Administrator/Desktop/datasets/non-linear.csv")
x = data.iloc[:, :-1].values

y = data.iloc[:, -1]


#plt.scatter(x, y)
# plt.show()
poly = PolynomialFeatures(degree=0)
p_x = poly.fit_transform(x)
# print(p_x)

m = LinearRegression()
m.fit(p_x, y)
print(m.score(p_x, y))
plt.scatter(x, y)
plt.plot(x, m.predict(p_x))
plt.show()
