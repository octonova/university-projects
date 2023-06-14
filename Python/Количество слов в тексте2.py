a = input()
b = set()
for line in a:
    a = map(str, line.split())
    a = set(a)
    for i in a:
        b.add(i)
print('\n', len(b))