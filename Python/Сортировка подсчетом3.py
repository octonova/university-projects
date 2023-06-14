def CountSort(A):
    ct = [0] * 101
    if len(A) > (2**105):
        print("ERROR!")
        return
    try:
        for x in A:
            ct[x] += 1
    except IndexError:
        print("ERROR!")
        return

    schcount = [0] * (max(A) + 1)
    for i in A:
        schcount[i] += 1
    for count in range(max(A) + 1):
        print((str(count) + ' ') * schcount[count], end='')
m = list(map(int, input().split()))
CountSort(m)
