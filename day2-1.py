with open("input.txt") as f:
    data = f.read().splitlines()

def day2_1(data):
    count = 0
    for line in data:
        occurance = line.split(" ")[2].count(line.split(" ")[1][0])
        Min = int(line.split(" ")[0].split('-')[0])
        Max = int(line.split(" ")[0].split('-')[1])

        if occurance in range(Min, Max + 1):
            count += 1

    print(count)

day2_1(data)
