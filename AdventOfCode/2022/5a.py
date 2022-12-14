stacks = []
movements = []
inputFile = "d:\\Coding\\AdventOfCode\\5input.txt"

def printStacks():
    global stacks
    for i in range(0, len(stacks)):
        print(i+1, stacks[i])

for i in range(0,9):
    stacks.append([])
    
with open(inputFile) as f:
    for line in f:
        if line.startswith('['):
            n = 4
            groups = [line[i:i+n].strip() for i in range(0, len(line), n)]
            for i in range(0,9):
                item = groups[i]
                if len(item) == 3:
                    item = item[1]
                    stacks[i].insert(0,item)
        elif line.startswith('move'):
            parts = line.strip().split(" ")
            movements.append([parts[1], parts[3], parts[5]])
        
printStacks()

for movement in movements:
    amount, source, destination = movement
    for i in range(int(amount)):
        item = stacks[int(source)-1].pop()
        stacks[int(destination)-1].append(item)

printStacks()

result = ""
for i in range(len(stacks)):
    result += stacks[i][len(stacks[i])-1]
    
print(result)
    