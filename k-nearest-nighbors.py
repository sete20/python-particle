import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data_classifier = pd.read_csv(
    "C:/Users/Administrator/Desktop/datasets/IRIS.csv")

x = data_classifier.iloc[:, :-1]
y = data_classifier.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.5)
model_classifier = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                                        metric_params=None, n_jobs=None, n_neighbors=5, p=2, weights='uniform').fit(x_train, y_train)
print(model_classifier.score(x_train, y_train))


data_regressor = pd.read_csv(
    "C:/Users/Administrator/Desktop/datasets/Stores.csv")
data_regressor = data_regressor.dropna()
x = data_regressor.iloc[:, :-1]
y = data_regressor.iloc[:, -1]

model_regressor = KNeighborsRegressor(n_neighbors=5).fit(x_train, y_train)
print(model_regressor.score(x_train, y_train))
