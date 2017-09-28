import subprocess


def getInput():
    pass

f = open('./main.c', 'a+')

command = input()
f.write("int main()\n")
f.write('{\n')
f.write(command + '\n')
f.write("return 0;\n")
f.write('}\n')
consoleOutput = subprocess.getstatusoutput("gcc " + f.name[2::] + " -o main")
if consoleOutput[0] is not 0:
    print(consoleOutput[1])
    exit(0)
print(consoleOutput[1])
