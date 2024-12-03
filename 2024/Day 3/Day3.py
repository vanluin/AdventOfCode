import re

inputFile = "input.txt"
inputTestFile = "input-test.txt"

inputStrings = []


def readInput(fileName):
	with open(fileName, "r", encoding="utf-8") as f:
		return (f.readlines())



def part1():
	inputString = readInput(inputFile)
	print(re.findall("mul\\((\\d+),(\\d+)\\)", "".join(inputString)))
	answers = sum([a*b for (a,b) in [(int(x), int(y)) for (x,y) in re.findall("mul\\((\\d+),(\\d+)\\)", "".join(inputString))]])
	print(answers)


def part2():
	pass

if __name__ == "__main__":
	part1()
	part2()
