with open('./data13.txt') as data:
	sum = 0
	for i in range(0,100):
		now = data.readline()
		now = int(now[0:50:1])
		sum += now
	print(sum)
