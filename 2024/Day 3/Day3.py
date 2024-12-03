import re

inputFile = "input.txt"
inputTestFile = "input-test.txt"

inputStrings = []


def readInput(fileName):
	with open(fileName, "r", encoding="utf-8") as f:
		return (f.readlines())


# Aan elkaar plakken van alle strings in de inputfile, mocht het over meerdere regels verspreid zijn
# Neem de som van alle producten van alle naar integer omgezette groepjes van twee getallen die tussen mul() staan
# Druk het antwoord af
def part1():
	inputString = "".join(readInput(inputFile))
	answer = sum([a*b for (a,b) in [(int(x), int(y)) for (x,y) in re.findall("mul\\((\\d+),(\\d+)\\)", inputString)]])
	print("Part 1:", answer)


# Aan elkaar plakken van alle strings in de inputfile, mocht het over meerdere regels verspreid zijn
# Splits de string op "do()", en knip van elk stukje alles achter een "don't()"'s van af, zodat je een string met alleen de tekst achter de do's overhoudt
# Neem de som van alle producten van alle naar integer omgezette groepjes van twee getallen die tussen mul() staan
# Druk het antwoord af
def part2():
	inputString ="".join(readInput(inputFile))
	cleanedString = "".join([x.split("don't()")[0] for x in inputString.split("do()")])
	answer = sum([a*b for (a,b) in [(int(x), int(y)) for (x,y) in re.findall("mul\\((\\d+),(\\d+)\\)", cleanedString)]])
	print("Part 2:", answer)


if __name__ == "__main__":
	part1()
	part2()
