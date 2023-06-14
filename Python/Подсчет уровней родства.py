n = int(input())

treePart = {}
for _ in range(1, n):
    line = input()
    child, parent = line.split()
    treePart[child] = parent
all_man = set(treePart.keys()) | set(treePart.values())
heights = {}


def f(z):
    if z not in treePart:
        heights[z] = 0
        return 0
    x = treePart[z]
    if x in heights:
        value = heights[x] + 1
    else:
        value = f(
            x) + 1
    heights[z] = value
    return value


for name in all_man:
    if name not in heights:
        f(name)

for name in sorted(heights):
    print(name, heights[name])