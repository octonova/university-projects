import sys
value = dict()
for valueLine in sys.stdin:
    valueLine = valueLine.split()
    if int(valueLine[1]) not in value:
        value[int(valueLine[1])] = set()
        value[int(valueLine[1])].add(valueLine[0])
    else:
        value[int(valueLine[1])] = set(value[int(valueLine[1])])
        value[int(valueLine[1])].add(valueLine[0])
value = dict(sorted(value.items(), key=lambda x: x[0]))
for valueKey in value:
    value[valueKey] = sorted(value[valueKey])
print(valueKey, *value[valueKey])