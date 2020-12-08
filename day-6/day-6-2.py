with open('input.txt') as f:
    data = f.read().split('\n\n')

l = []
a = 0
for line in data:
    C = line.replace('\n','')
    L = {}
    for c in C:
        if c in L.keys():
            L[c] += 1
        else:
            L[c] = 1

    for _ , count in L.items():
        if count == len(line.split('\n')):
            a += 1

l.append(a)
print(sum(l))
