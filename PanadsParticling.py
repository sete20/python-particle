import pandas as pa
"""panads lib particling"""
# ls = ["1", "2", "3", "4", "5", "6", "100000", "100000"]
ls = [1, 2, 3, 4, 5, 6, 100000, 100000]

ser = pa.Series(ls)

# print(ser.index)
# print("******"*50)
# # print(ls)
# print(ser.values)

# print("******"*50)
# print(ls)
print(ser.describe())
print("******"*20)
print(ser.sum())
print("******"*20)
print(ser.agg(['min', 'std']))

print("******"*20)
print(pa.DataFrame(ser))
