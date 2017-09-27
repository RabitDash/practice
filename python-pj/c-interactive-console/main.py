import subprocess


def getInput():
    pass

f = open('./main.c', 'r+')

while f.readline() != 'int main()\n':
    f.readline()

fileStart = f.tell()
print(fileStart)
command = input()
f.write('{\n')
f.write(command + '\n')
f.write("return 0;\n")
f.write('}\n')
consoleOutput = subprocess.getstatusoutput("gcc " + f.name[2::] + " -o main")
if consoleOutput[0] is not 0:
    print(consoleOutput[1])
    exit(0)
subprocess.getoutput("chmod +x main")
consoleOutput = subprocess.getstatusoutput("./main")
print(consoleOutput[1])