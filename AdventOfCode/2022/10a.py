register = [1]
commands = []
with open("10input.txt", "r") as f:
    for line in f:
        commands.append(line.strip())

def doNoop():
    global register
    curVal = register[len(register)-1]
    register.append(curVal)
   
def doAddx(x):
    global register
    doNoop()
    curVal = register[len(register)-1]
    register.append(curVal+x)

for command in commands:
    if command == "noop":
        doNoop()
    else:
        amount = int(command.split(" ")[1])
        doAddx(amount)

result = 0
for i in range(20, 221, 40):
    result += register[i-1] * i

print(result)
