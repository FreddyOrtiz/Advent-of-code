with open("input.txt") as f:
	a = [int(f.readline()[:-1]) for i in range(200)]
	
for i in a:
	for j in a:
		for k in a:
			if i + j + k  == 2020:
				print(i*j*k)
			else:	
				pass
