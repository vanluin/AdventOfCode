
inputFile = "input.txt"
inputTestFile = "input-test.txt"


def readinput(fileName):
	with open(fileName, "r", encoding="utf-8") as f:
		return f.readlines()


def checkfield(field, position, direction, text):
	newposition = tuple(a+b for a,b in zip(position, direction))

	# Controleren of we niet over de randen gaan
	if newposition[0] < 0 or newposition[0] > len(field)-1 or newposition[1] < 0 or newposition[1] > len(field[0])-1:
		return False

	# Als we de correcte letter gevonden hebbem:
	if field[newposition[0]][newposition[1]] == text[0]:
		# Als het de laatste letter was, zijn we klaar.
		if len(text) == 1:
			return True
		# en anders gaan we vanaf de nieuwe positie in dezelfde richting verder zoeken
		else:
			return checkfield(field, newposition, direction, text[1:])


def part1():
	inputstrings = [x.strip() for x in readinput(inputFile)]
	aantalgevonden = 0
	for row, line in enumerate(inputstrings):
		# alle posities van de letter X in de regel
		positions = [x for x, c in enumerate(line) if c == 'X']
		# controleer per positie de 8 richtingen
		for position in positions:
			for direction in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
				found =  checkfield(inputstrings, (row, position), direction, "MAS")
				if found:
					aantalgevonden += 1

	print("Part 1:", aantalgevonden)


def part2():
	inputstrings = [x.strip() for x in readinput(inputFile)]
	aantalgevonden = 0
	for row, line in enumerate(inputstrings):
		# De letter A mag niet in de bovenste of onderste regel zitten
		if row < 1 or row > len(inputstrings)-2:
			continue

		# alle posities van de letter A in de regel bepalen
		positions = [x for x, c in enumerate(line) if c == 'A']

		# Per positie bekijken of er een X-MAS kan zijn
		for col in positions:
			# De A mag ook niet in de eerste of laatste kolom zitten
			if col < 1 or col > len(inputstrings[0])-2:
				continue

			# De vier hoekpunten berekenen
			directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
			corners = list(map(lambda direction: (row + direction[0], col + direction[1]), directions))

			# De bijhorende letters uit het grid halen
			lb, rb, lo, ro = list(map(lambda corner: inputstrings[corner[0]][corner[1]], corners))

			# En nu kijken of de tegenover elkaar liggende letters "MS" of "SM" vormen
			if lb + ro in ["MS", "SM"] and rb + lo in ["MS", "SM"]:
				aantalgevonden += 1

	print("Part 2:", aantalgevonden)


if __name__ == "__main__":
	part1()
	part2()
