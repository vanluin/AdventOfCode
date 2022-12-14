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

crt_line = ""
for i in range(len(register)):
    sprite_pos = register[i]
    crt_pos = i % 40
    if abs(sprite_pos-crt_pos) <= 1:
        crt_line += "#"
    else:
        crt_line += "."
    if i % 40 == 39:
        print(crt_line)
        crt_line = ""


    