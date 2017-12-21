maxi = 0
max2 = 0
for i in range(5,1000001):
	now = 0
	n = i
	while n > 1:
		if n % 2 == 0:
			n = n / 2
			n = int(n)
			now += 1
			continue
		if n % 2 == 1:
			n = 3 * n + 1
			now += 1
			continue
	if now > maxi:
		maxi = now
		if max2 < i:
			max2 = i
print(max2)
