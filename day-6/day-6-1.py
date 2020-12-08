with open('input.txt') as f:
    data = f.read().split('\n\n')

l = []

for line in data:
    a = {}
    C = line.replace('\n','')
    for c in C:
        if c in a.keys():a[c] += 1
        else:a[c] = 1
    l.append(len(a))

print(sum(l))
