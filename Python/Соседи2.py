import sys
d = 0
a = int(input("Value:"))
b = input("Value:").split()
experctedLength = a
if len(b) == experctedLength:
    for c in range(1, len(b) - 1):
        if int(b[c]) - int(b[c-1])>0 and int(b[c]) - int(b[c+1])>0:
            d += 1
        print(d, end="")
elif len(b) != experctedLength:
    print("Error!")
sys.exit (1)