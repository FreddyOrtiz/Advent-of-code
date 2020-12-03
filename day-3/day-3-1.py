with open("input.txt") as f:
    data = f.read().splitlines()

dx,dy = 0, 0
count = 0

for line in data:
    if line[dx % len(line)] == "#":
        count += 1
    dx += 3
    dy += 1

print(count)
