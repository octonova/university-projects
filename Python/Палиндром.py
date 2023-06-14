k = int(input("Number:"))
countNumber = 0
countFlip = 0
if 1 <= k <= 100000:
    for countNumber in range(1, k+1):
        number = countNumber
        flip = 0
        while number > 0:
            flip = flip * 10 + number % 10
            number = number // 10
        if countNumber == flip:
            countFlip += 1
    print(countFlip)
else:
    print("ERROR!")
