def checkNumber(string):
    string = string.replace('-', '').replace('(', '').replace(')', '')
    return string[-10:] \
        if len(string) > 7 \
        else '495' + string[-7:]


n = 4
notes = [input() for _ in range(n)]
for note in notes[1:]:
    print('YES' if checkNumber(notes[0]) == checkNumber(note) else 'NO')