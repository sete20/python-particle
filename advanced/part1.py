from ast import stmt
import timeit


print(__name__) # direct === main extended === name
# print(dir(timeit))
# print(timeit.repeat("'hi' * 1000",repeat=10))
print(timeit.repeat(stmt="random.randint(0,50)",setup="import random",repeat = 5))
