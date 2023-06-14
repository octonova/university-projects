print(*list(map(lambda xi: (xi[0] + xi[1]) % 2,
                zip(map(int, input().split()), map(int, input().split())))))