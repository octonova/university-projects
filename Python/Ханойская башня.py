def towerHanoi(n, i, j):
    if n <= 0:
        return
    k = 6 - i - j
    towerHanoi(n-1, i, k)
    print(n, i, j)
    towerHanoi(n-1, k, j)


try:
    n = int(input())
except ValueError:
    print("Error!")
else:
    towerHanoi(n, 1, 3)

