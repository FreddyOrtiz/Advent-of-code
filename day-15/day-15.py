a = [1,20,11,6,12,0]
N = 2020

for i in range(N-len(a)):
	if a.count(a[-1]) <= 1:	
		a.append(0)
	else:
		aa = []
		for n, j in enumerate(a):
			if j == a[-1]:
				aa.append(n+1)
		a.append(aa[-1] - aa[-2])

print(a[-1])
