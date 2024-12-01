commands = []
dirstruct = {"name":"/", "parent":None, "dirs":[], "files":[], "totalsize":0}

def readInput():
    global commands
    inputFile = "d:\\Dropbox\\Python\\AdventOfCode\\7input.txt"        
    with open(inputFile) as f:
        for line in f:
            commands.append(line.strip())

def parseCommands():
    global commands
    global dirstruct
    curdir = dirstruct
    
    for command in commands:
        if command == "$ cd /":
            continue
        elif command == "$ ls":
            continue
        elif command.startswith("dir"):
            continue
        elif command == "$ cd ..":
            curdir = curdir["parent"]
        elif command.startswith("$ cd"):
            dirname = command[5:]       
            newdir = {"name":dirname, "parent":curdir, "dirs":[], "files":[], "totalsize":0}
            curdir["dirs"].append(newdir)
            curdir = newdir
        elif command[0].isdigit():
            size, filename = command.split(" ")
            curdir["files"].append({"filename":filename, "size":size})

def computeTotalSizeOfDir(dir):
    totalsize = 0
    for file in dir["files"]:
        totalsize += int(file["size"])
    
    for subdir in dir["dirs"]:
        totalsize += computeTotalSizeOfDir(subdir)
    
    dir["totalsize"] = totalsize
    return totalsize
    
def findDirectoriesAboveTarget(dir, targetSize):
    candidates = []
    if dir["totalsize"] >= targetSize:
        candidates.append(dir)
    
    for subdir in dir["dirs"]:
        for candidate in findDirectoriesAboveTarget(subdir, targetSize):
            candidates.append(candidate)
    
    return candidates

readInput()
parseCommands()
computeTotalSizeOfDir(dirstruct)


totalSpace = 70000000
requiredSpace = 30000000
unusedSpace = totalSpace - dirstruct['totalsize']
missingSpace = requiredSpace - unusedSpace

candidates = findDirectoriesAboveTarget(dirstruct, missingSpace)

smallestSize = totalSpace
smallestName = "all"
for candidate in candidates:
    if candidate["totalsize"] < smallestSize:
        smallestName = candidate["name"]
        smallestSize = candidate["totalsize"]

print(smallestName, smallestSize)

