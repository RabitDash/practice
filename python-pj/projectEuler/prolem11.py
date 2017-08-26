#!/usr/bin/env python

with open("/home/animaze/workspace/python-projects/data10.txt", "r") as data:
	def readlist(data):
		tmp = data.readline()
		tmp = tmp[0:59:1]
		data_list = list(map(int, tmp.split(' ')))
		return data_list

	def aread(data):
		data_array = []
		for counter in range(0, 20):
			data_array.append(readlist(data))
		return data_array
	maximum = 0
	array = aread(data)
	data.close()
	for x in range(0, 16):
		for y in range(0, 16):
			#print((x,y))
			raw = array[x][y]*array[x+1][y]*array[x+2][y]*array[x+3][y]
			line = array[x][y]*array[x][y+1]*array[x][y+2]*array[x][y+3]
			diagl = array[x][y]*array[x+1][y+1]*array[x+2][y+2]*array[x+3][y+3]
			diagr = array[x][20 - y - 1] * array[x + 1][20 - y - 2] * array[x + 2][20 - y - 3] * array[x + 3][20 - y - 4]
			#print(line, raw, diag)
			if maximum < max(line, raw, diagl,diagr):
				maximum = max(line, raw, diagl,diagr)
	print(maximum)