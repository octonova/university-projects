try:
    a, b, c, d = map(int, input().split())
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    s = set()
    st = set()
    for i in range(a, b + 1):
        s.add(i)
    for i in range(c, d + 1):
        st.add(i)
    print(len(s & st))
except ValueError:
    print("Error!")