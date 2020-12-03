with open("input.txt") as f:
    data = f.read().splitlines()

dx = 0
dy = 0
trees = 0

for line in data:
    if line[dx % len(line)] == "#":
        trees += 1
    dx += 3
    dy += 1

print(trees)
