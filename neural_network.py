import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import
data = pd.read_csv("C:/Users/Administrator/Desktop/datasets/iris.csv")
# print(data.isnull().sum())
# data.describe()
x = data.iloc[:, :-1]
y = data.iloc[:, -1]
x_obj = x.select_dtypes(include=["object"])


x_non_obj = x.select_dtypes(exclude=["object"])

la = LabelEncoder()
for i in range(x_obj.shape[1]):
    x_obj.iloc[:, i] = la.fit_transform(x_obj.iloc[:, i])

X = pd.concat([x_non_obj, x_obj], axis=1)

x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.95)

#model = LogisticRegression(multi_class="ovr").fit(x_train,y_train)
model = OneVsRestClassifier(
    estimator=LogisticRegression()).fit(x_train, y_train)

print(model.score(x_train, y_train))
print(model.score(x_test, y_test))
