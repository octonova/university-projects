a = int(input())
p_factorial = 1
p_sum = 0
for b in range(1, a + 1):
    p_factorial *= b
    p_sum += p_factorial
print(p_sum)