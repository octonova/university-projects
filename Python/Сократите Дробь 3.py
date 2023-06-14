def ReduceFraction(n, m):
    x1 = max(n, m)
    y1 = min(n, m)
    if x1 == y1 and x1 * y1 != 0:
        return 1, 1
    else:
        z = x1 % y1
        while z > 0:
            x1 = y1
            y1 = z
            z = x1 % y1

        return n // y1, m // y1


n, m = map(int, input().split())
print(*ReduceFraction(n, m))
