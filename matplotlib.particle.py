from this import s
from matplotlib import projections
import matplotlib.pyplot as plt
import numpy as np
# x = [100, 200, 300, 400, 500]
# y = [1000, 100, 3000, 300, 10]
# plt.plot(x, y)
# plt.show()
# plt.style.use("seaborn")
# area = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

# price = np.array([10, 12, 20, 22, 21, 25, 30, 21, 32, 34, 35])

# plt.scatter(x=area, y=price, marker='.', color='g', s=150)
# plt.show()


# precentage = [1, 2, 3, 4, 5]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(precentage, marks,
#         labeldistance=1.1,
#         explode=myexplode,
#         autopct=True,
#         radius=1.1,
#         startangle=0,
#         colors=[
#             'red', 'blue', 'green', 'black', 'y'])
# y = np.array([20, 15, 15, 30, 20])
# marks = ['dacani', 'nestla', 'aquafina', 'anything else 1', 'somthing else 2']
# myexplode = [0.11, 0.11, 0.11, 0.11, 0.11]

# plt.pie(y, labels=marks, explode=myexplode, radius=1.1,
#         startangle=180, colors=['r', 'g', 'b', 'gray', 'y', ], autopct=' % .2f')
# plt.show()
# autocpt to show precentage
#  explode the space betwen the attrs
# startangle لتحديد من اين تبدا الدائرة
# marks = ['dacani', 'nestla', 'aquafina', 'anything else 1', 'somthing else 2']
# prices = [0.11, 0.11, 0.11, 0.11, 0.11]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.array([100, 200, 300, 400, 500])
y = np.array([1000, 3000, 5000, 2000, 10000])
z = np.array([1, 2, 3, 4, 10])
ax.plot3D(x, y, z, 'red')

ax.scatter3D(x, y, z, c='black')

plt.show()
# data = np.array([[' mohamed ', ' abdelrhman'], [' mohamed ', ' mohamed ',
#                 ' abdullah '], ['ali', 'omar'], ['othman', ' mohamed '], ])

# plt.hist(data, histtype='stepfilled', alpha=.5, bins=11)
# plt.show()
# x = ['Saturday', 'sunday',  "Monday",
#      "Tuesday", "Wednesday", "Thursday", "friday"]
# y = [12000, 10000, 8000, 8000, 9000, 8000, 7000]
# plt.xlabel("DAY")
# plt.ylabel("COUNT")
# الاسكتر للرسم البياني
# plt.scatter(x, y, color="blue", marker='x', s=100)
# # البلوت للخطوط والتقاطع
# plt.plot(x, y, color="black")
# # البار للبارات
# plt.bar(x, y, edgecolor="blue", facecolor="yellow")
# plt.show()
# myexplode = [0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11]
# plt.pie(y, labels=x, explode=myexplode, radius=1.1,
#         startangle=180, autopct=' % .2f')
# plt.plot(x, y, color="black")
# plt.bar(x, y, edgecolor="blue", facecolor="yellow")

plt.show()
