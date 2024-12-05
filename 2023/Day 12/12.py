import functools
from re import findall
inputFile = r"input.txt"

def readInput():
    lines = [x.strip() for x in open(inputFile, "r", encoding="utf-8").read().split("\n") if x.strip() != '']
    return lines

@functools.cache 
def checkValidLine(line, config):
    # Checken of de springs op een regel overeenkomen met de vereiste configuratie
    groups = findall(r'#+', line)
    configGroups = config.split(",")
    if len(groups) != len(configGroups):
        # Als het aantal groepjes springs niet overeenkomt met het aantal in de configuratie, dan fout
        return False
    for index, spring in enumerate(groups):
        # Per groepje kijken of het overeenkomt
        if len(spring) != int(configGroups[index]):
            return False
    return True


@functools.cache 
def generateValidOptions(line, config):
    validOptions = []
    options = [line]
    while len(options) > 0:
        option = options.pop()
        if "?" in option:
            index = option.find("?")
            l = list(option)
            l[index] = "#"
            options.append("".join(l))
            l[index] = "."
            options.append("".join(l))
        else:
            if checkValidLine(option, config):
                validOptions.append(option)
                
    return validOptions

def part1(lines):
    result = 0
    for line in lines:
        springs, config = line.split(" ")
        validOptions = generateValidOptions(springs, config)
        #print(len(validOptions), validOptions, config)
        result += len(validOptions)
    print("Part 1:", result)

def part2(lines):
    result = 0
    
    print("Part 2:", result)
        
    
lines = readInput()
part1(lines)
part2(lines)