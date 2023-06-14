try:
    print(len(set(map(int, input().split()))))
except ValueError:
    print("Error!")