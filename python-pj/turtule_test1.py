import turtle as t
import sys
def draw(length, bian):
    angle = 360 / bian
    for i in range(bian):
        t.fd(length)
        t.right(angle)
draw(100,4)
