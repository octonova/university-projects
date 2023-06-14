import sys


data = dict()
for line in sys.stdin:
    line = line.split()
    if int(line[1]) not in data:
        data[int(line[1])] = set()
        data[int(line[1])].add(line[0])
    else:
        data[int(line[1])] = set(data[int(line[1])])
        data[int(line[1])].add(line[0])

data = dict(sorted(data.items(), key=lambda x: x[0]))


for key in data:
    data[key] = sorted(data[key])
    print(key,*data[key])
