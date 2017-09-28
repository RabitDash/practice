#!/usr/bin/env python3
import subprocess as sp

src = sp.getoutput("ls src/").split('\n')  # list
for file in src:
    if file.find(".h") is not -1:
        src.remove(file)

for file in src:
    sp.getoutput("gcc " + "-c src/" + file + " -o " + "obj/" + file.split(".c")[0] + ".o")

obj = sp.getoutput("ls obj/").split('\n')  # list
objects = ""
for file in obj:
    objects += "obj/" + file + " "
print(objects)
sp.getoutput("gcc " + objects + " -o " + "bin/" + "main")

