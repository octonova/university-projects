print(" ".join(map(str, filter(lambda x: all(map(lambda y: x % y != 0, range(2, x))),
                               range(2, int(input()) + 1)))))