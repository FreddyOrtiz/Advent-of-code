def fun(text):
    a = []
    for i in text:
        if i == 'F' or i == 'L':
            a.append('0')
        elif i == 'B' or i == 'R':
            a.append('1')
    return ''.join(a)

with open("input.txt") as f:
    data = f.read().splitlines()
    b = []
    for line in data:
        row = int(fun(line[:7]), 2)
        col = int(fun(line[-3:]),2)
        index = row * 8 + col
        b.append(index)

print(max(b))
