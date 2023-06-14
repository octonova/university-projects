d = [0]*10
while True:
    d[int(input())] += 1
    if d[0]:
        break
print(*d[1:])