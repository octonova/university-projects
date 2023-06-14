a = 1
def f():
    global a
    b = int(input())
    if b:
        f()
    for c in range(1, b + 1):
        if c * c == b:
            print(b)
            a += 1
f()
if a == 1:
    print(0)