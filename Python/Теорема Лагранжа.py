def lagrange(x, z, q):
    b = int(x ** (1 / z))
    if x - b ** z == 0:
        return str(b)
    if q == 1:
        return 0
    while lagrange(x - b ** z, z, q - 1) == 0:
        b -= 1
        if b <= 0:
            return 0
    return str(b) + ' ' + lagrange(x - b ** z, z, q - 1)


try:
    n = int(input())
    if n > 10000:
        print("Value > 10000")
    else:
        print(lagrange(n, 2, 4))
except ValueError:
    print("Error!")