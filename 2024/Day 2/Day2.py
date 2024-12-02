inputFile = "input.txt"
inputTestFile = "input-test.txt"

inputStrings = []


def readInput(fileName):
	with open(fileName, "r", encoding="utf-8") as f:
		return (f.readlines())


# Deze functie checkt of de levels in de lijst strikt stijgend of dalend zijn en of het verschil
# niet groter is dan 3. Via de optionele parameter "allowed_errors" kan worden meegegeven hoeveel
# fouten in de lijst toegestaan zijn.
def checkLevels(levels, direction, allowed_errors=0):
	correct = True

	# Wandel de hele lijst af
	for i in range(len(levels) - 1):
		# Bepaal steeds het verschil tussen de huidige positie en de volgende
		difference = levels[i + 1] - levels[i]

		# Controleren of het verschil niet 0 is, maar wel maximaal 3 en of het in de goede richting is
		if difference == 0 or abs(difference) > 3 or (int(difference / abs(difference)) != direction):
			# Zo niet, als het maximale aantal fouten nog niet bereikt is, probeer dan eerst de ene,
			# en dan de andere van de twee weg te laten. Zodra een correcte gevonden is zijn we klaar.
			# Deze oplossing staat toe dat meerdere gedempte fouten mogelijk ondersteund worden.
			if allowed_errors > 0:
				newLevels = levels.copy()
				newLevels.pop(i)
				correct = checkLevels(newLevels, direction, allowed_errors - 1)
				if not correct:
					newLevels = levels.copy()
					newLevels.pop(i+1)
					correct = checkLevels(newLevels, direction, allowed_errors - 1)
			else:
				correct = False
				break
	return correct


def part1():
	countSafe = 0
	inputStrings = readInput(inputFile)
	for report in inputStrings:
		# Omzetten naar lijst van integers
		levels = [int(x) for x in report.strip().split(" ")]

		# Als de lijst dubbelen bevat dan sowieso overslaan
		if len(set(levels)) != len(levels):
			continue

		# Bepalen van de richting van de lijst
		direction = int((levels[1]-levels[0])/abs(levels[1]-levels[0]))

		# En nu de levels checken zonder dat er een fout in de lijst mag zitten (allowed_errors default op 0)
		correct = checkLevels(levels, direction)

		if correct:
			countSafe += 1

	print("Part 1:", countSafe)


def part2():
	countSafe = 0
	inputStrings = readInput(inputFile)
	for index, report in enumerate(inputStrings):
		# Omzetten naar lijst van integers
		levels = [int(x) for x in report.strip().split(" ")]

		# De richting bepalen. Omdat één dubbele nu zou mogen, bij een direction van 0 nogmaals proberen maar
		# nu met één positie verder. Twee dubbelen mogen niet, dus dan overslaan.
		difference = levels[-1] - levels[0]
		if difference == 0:
			difference = levels[-2] - levels[0]
		if difference == 0:
			continue
		direction = int(difference/abs(difference))

		# En nu de levels checken met een "allowed_errors" van 1
		correct = checkLevels(levels, direction, 1)

		if correct:
			countSafe += 1

	print("Part 2:", countSafe)

if __name__ == "__main__":
	part1()
	part2()
