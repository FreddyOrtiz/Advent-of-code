with open('input.txt') as f:
	data = [int(i) for i in f.read().split('\n')[:-1]]

for index_of_number, number in enumerate(data):
    if index_of_number >= 25:
        IT_IS = 0
        num = data[index_of_number - 25: index_of_number]
        for n, i in enumerate(num):
            for N, j in enumerate(num):
                if n > N:
                    if i + j == number:
                        IT_IS = 1
        if not IT_IS:
            print(number)
