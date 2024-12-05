from math import lcm
from functools import reduce

inputFile = [r"input.txt", r"input.txt"]

def readInput(part):
    lines = open(inputFile[part], "r", encoding="utf-8").read().split("\n\n")
    return lines

def part1(lines):
    result = 0
    
    instructions, networkStrings = [x.strip() for x in lines]
    networkStrings = [x.replace(" = ", " ").replace("(", "").replace(")","").replace(",","") for x in networkStrings.split("\n")]
    
    network = {}
    for rule in networkStrings:
        node, left, right = rule.split(" ")
        network[node] = { "L":left, "R":right }
    
    stepCount = 0
    currentNode = "AAA"
    while currentNode != "ZZZ":
        instruction = instructions[stepCount % len(instructions)]
        #print("Van",currentNode,"richting",instruction,"komt uit bij",network[currentNode][instruction])
        currentNode = network[currentNode][instruction]
        stepCount += 1
    
    result = stepCount
    print("Part 1:", result)

def part2(lines):
    result = 0
    instructions, networkStrings = [x.strip() for x in lines]
    networkStrings = [x.replace(" = ", " ").replace("(", "").replace(")","").replace(",","") for x in networkStrings.split("\n")]
    
    network = {}
    for rule in networkStrings:
        node, left, right = rule.split(" ")
        network[node] = { "L":left, "R":right }
    
    stepCounts = []
    startNodes = [node for node in network if node.endswith("A")]
    for startNode in startNodes:
        stepCount = 0
        currentNode = startNode
        while not currentNode.endswith("Z"):
            instruction = instructions[stepCount % len(instructions)]
            currentNode = network[currentNode][instruction]
            stepCount += 1
        print("StartNode",startNode,"eindigt na",stepCount,"stappen")
        stepCounts.append(stepCount)
    
    # Nu we de lengte van alle individuele routes van een "A" node naar een "Z" node kennen,
    # kunnen we met de functie "kleinst gemene veelvoud" (herhaald toegepast op de lijst stepCounts)
    # het antwoord berekenen.
    result = reduce(lcm, stepCounts)
    print("Part 2:", result)
        
    
lines = readInput(0)
part1(lines)
lines = readInput(1)
part2(lines)