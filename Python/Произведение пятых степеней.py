from functools import reduce
print(reduce(lambda a, b: a * (b ** 5), [1] + list(map(int, input().split()))))