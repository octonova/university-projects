def summary(z=0):
    number = -1
    try:
        number = int(input())
    except ValueError:
        print("Error!")
    else:
        z += number
    if number != 0:
        return summary(z)
    return z


print(summary())