import sys
a = int(input("Value:"))
b = input("Value:").split()
experctedLength = a
for c in range(0, len(b), 2):
    if len(b) == experctedLength:
        print(b[c])
    elif len(b) != experctedLength:
        print("Error!")
sys.exit (1)
