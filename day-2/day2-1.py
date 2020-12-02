with open("input.txt") as f:
    data = f.read().splitlines()

def day2_1(data):
    count = 0
    for line in data:
        this = line.split(" ")[2].count(line.split(" ")[1][0])
        if this in range( int(line.split(" ")[0].split('-')[0]), ( int(line.split(" ")[0].split('-')[1]) + 1)):
            count += 1

    print(count)

day2_1(data)
