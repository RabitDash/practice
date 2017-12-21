#!/usr/bin/env python
prev = 1
preprev = 1
num = 0
now = 0
while(now <= 4000000):
    now = prev + preprev
    if(now % 2 == 0):
        num += now
    preprev,prev = prev,now
print(num)
