# What is the number of 1-jolt positions{0} differences
# multiplied by the number of 3-jolt differences positions{2}?

with open("input.txt", "r") as f:
    nums = sorted([int(line) for line in f.read().strip().split("\n")])

positions = [0,0,1]
pos = 0

for num in nums:
    positions[num - pos - 1] += 1
    pos = num
    

print(positions[0] * positions[2])
