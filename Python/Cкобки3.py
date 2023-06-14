value = input()


def sortedValue (x1: str) -> bool:
    stackValue = []
    for y1 in x1:
        if y1 in ("(", "{", "("):
            stackValue.append(y1)
        if y1 == ")":
            head = stackValue.pop()
            if head != "(":
                return False
        if y1 == "}":
            head = stackValue.pop()
            if head != "{":
                return False
    return len(stackValue) == 0


try:
    if sortedValue(value) == 1:
        print(0)
    else:
        print(1)
except IndexError:
    print(1)