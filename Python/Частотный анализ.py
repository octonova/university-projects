import sys

letS = (str(sys.stdin.read()).split())
myLets = {}
for let in letS:
    myLets[let] = myLets.get(let, 0) + 1
myLets = [(fr, lt) for lt, fr in myLets.items()]


def sort(lws):
    return -lws[0], lws[1]


myLets.sort(key=sort)
for i in range(len(myLets)):
    print(myLets[i][1])