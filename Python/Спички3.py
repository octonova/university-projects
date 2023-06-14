l1, r1, l2, r2, l3, r3 = map(int, input().split())
if r1 >= l2 and (r2 >= l3 or r3 >= l1):
    print(0)
elif (r2 + r1 - l1 >= l3):
    print(1)
elif (r1 + r3 - l3 >= l2):
    print(3)
elif (r2 + r1 - l1 >= l3) and (r1 + r3 - l3 >= l2):
    print(1)
else:
    print(-1)