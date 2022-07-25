import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data_classifier = pd.read_csv(
    "C:/Users/Administrator/Desktop/datasets/IRIS.csv")

x = data_classifier.iloc[:, :-1]
y = data_classifier.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.95)
model_classifair = RandomForestClassifier(
    n_estimators=10, max_depth=10).fit(x_train, y_train)
print(model_classifair.score(x_train, y_train))
print(model_classifair.score(x_test, y_test))
print('end classification and start regression')
print('*' * 50)

data_classifier = pd.read_csv(
    "C:/Users/Administrator/Desktop/datasets/Stores.csv")

x = data_classifier.iloc[:, :-1]
y = data_classifier.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.85)

model_regression = RandomForestRegressor(n_estimators=50).fit(x_train, y_train)
print(model_regression.score(x_train, y_train))
