#!/usr/bin/env python
maxi = '0'
for i in range(100,999):
	for j in range(100,999):
		x = str(i * j)
		if((x == x[::-1]) & (int(x) > int(maxi))):
			maxi = x
print(maxi)
