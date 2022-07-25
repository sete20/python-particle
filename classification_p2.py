import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("C:/Users/Administrator/Desktop/datasets/heart_failure_clinical_records_dataset.csv")
#print(data.isnull().sum())

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.95)
model = LogisticRegression()
model.fit(x_train,y_train)
print(model.score(x_train,y_train))
#print(x_train)
print(model.score(x_test,y_test))