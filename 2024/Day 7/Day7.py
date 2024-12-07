
inputFile = "input.txt"
inputTestFile = "input-test.txt"

# Recursief controleren of het tussengetal + of * de eerstvolgende uit de lijst numbers leidt tot het doel
# Via number_index wordt bijgehouden waar in de numbers lijst we gebleven zijn.
def checkEquation(goal, numbers, number_index=0, intermediate=0):
	# We kunnen stoppen wanneer:
	# - het tussengetal groter is dan het doel
	# - we het einde van de lijst numbers bereikt hebben
	if intermediate > goal or number_index >= len(numbers):
		return intermediate == goal

	# Is het doel niet bereikt en hebben we nog nummers over in de lijst,  check dan
	# zowel + als * het eerstvolgende getal
	currentNumber = numbers[number_index]
	return (checkEquation(goal, numbers, number_index+1, intermediate+currentNumber) or
			checkEquation(goal, numbers, number_index+1, intermediate*currentNumber))

# Vergelijkbaar met checkEquation, alleen wordt hier wanneer het doel nog niet bereikt is
# ook gecheckt of we het doel kunnen halen door het eerstvolgende getal aan het huidige
# tussenresultaat te plakken
def checkEquation2(goal, numbers, number_index=0, intermediate=0):
	if intermediate > goal or number_index >= len(numbers):
		return intermediate == goal

	currentNumber = numbers[number_index]
	return (checkEquation2(goal, numbers, number_index+1, int(str(intermediate)+str(currentNumber))) or
			checkEquation2(goal, numbers, number_index+1, intermediate+currentNumber) or
			checkEquation2(goal, numbers, number_index+1, intermediate*currentNumber))


def part1():
	lines = [x.strip() for x in open(inputFile).read().split("\n")]
	answer = 0
	for line in lines:
		goal, numbers = line.split(": ")
		goal = int(goal)
		numbers = [int(x.strip()) for x in numbers.split(" ")]
		correct = checkEquation(goal, numbers)
		if correct:
			answer += goal

	print("Part 1:", answer)


def part2():
	lines = [x.strip() for x in open(inputFile).read().split("\n")]
	answer = 0
	for line in lines:
		goal, numbers = line.split(": ")
		goal = int(goal)
		numbers = [int(x.strip()) for x in numbers.split(" ")]
		correct = checkEquation2(goal, numbers)
		if correct:
			answer += goal

	print("Part 2:", answer)


if __name__ == "__main__":
	part1()
	part2()