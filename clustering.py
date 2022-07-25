import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster
data = pd.read_csv("C:/Users/Administrator/Desktop/datasets/Iris.csv")
#print(data.isnull().sum())

x = data.iloc[:,:-1]
j=[]
cost_num = []
for i in range(1,10):
    model =  cluster.KMeans(n_clusters=i).fit(x)
    cost_num.append(i)
    j.append(model.inertia_)

plt.plot(cost_num,j)    
plt.show()
print(j)
print(cost_num)