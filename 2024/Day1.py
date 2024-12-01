import re

dag = "1"
inputFile = "input"+dag+".txt"
inputTestFile = "input"+dag+"-test.txt"

inputStrings = []
def readInput(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        return(f.readlines())

def part1and2():
    leftList = []
    rightList= []
    inputStrings = readInput(inputFile)
    for pair in inputStrings:
        x,y = re.split(" +", pair)
        leftList.append(int(x.strip()))
        rightList.append(int(y.strip()))
    leftList.sort()
    rightList.sort()
    sortedList = zip(leftList, rightList)

    result = sum([abs(x-y) for x,y in [z for z in sortedList]])
    print("Part 1", result)

    result = sum([x * len([y for y in rightList if y == x]) for x in leftList])
    print("Part 2", result)

    result = sum([x * rightList.count(x) for x in leftList])
    print("Part 2.1", result)

if __name__ == "__main__":
    part1and2()