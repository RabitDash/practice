#!/usr/bin/env python
import math

for a in range(1,1000):
	for b in range(1,1000):
			if (a < b < (1000 - a - b)) & (a**2 + b**2 == (1000 - a - b)**2):
				print(a, b)
			
