
inputFile = "input.txt"
inputTestFile = "input-test.txt"

orders = []

# Deze functie checkt of alle combinaties van 2 pagina's niet omgekeerd in de lijst verplichte volgordes staan.
# Is er wel tenminste één omgekeerde combinatie in de lijst verplichte volgordes, dan is de niet-omgekeerde volgorde
# dus foutief.
def checkCorrect(pages):
	global orders

	combinations = [(pages[x], pages[y]) for x in range(len(pages) - 1) for y in range(x + 1, len(pages))]
	correct = not (any([y + "|" + x in orders for (x, y) in combinations]))
	return correct


def part1():
	global orders

	# Scheidslijn tussen volgordes en manuals is een dubbele regelovergang
	orderstring, manualstring = open(inputFile).read().strip().split("\n\n")
	# Volgordes en manuals omzetten naar lijsten
	orders = orderstring.split("\n")
	manuals = manualstring.split("\n")

	# Het idee hier is dat we van een manual alle combinaties van pagina's controleren.
	# Voor alle combinaties van 2 pagina's geldt dat de omgekeerde volgorde niet in de lijst volgordes mag staan.
	# Dus als in een manual pagina 75 vóór pagina 97 staat, mag "97|75" niet in de lijst volgordes staan, en dat voor
	# alle combinaties van 2 pagina's in de manual.
	# Blijkt een manual goed, dan tellen we de middelste op bij het antwoord.
	answer = 0
	for manual in manuals:
		pages = manual.split(",")
		correct = checkCorrect(pages)
		if correct:
			answer += int(pages[len(pages)//2])

	print("Part 1:", answer)


def reorder_pages(pages):
	global orders

	# Herhalen zolang de pages nog niet in de juiste volgorde staan
	while not checkCorrect(pages):
		# Controleer alle combinaties van 2 pagina's
		for x in range(len(pages)-1):
			for y in range(x+1, len(pages)):
				# Als ze in een verboden volgorde staan (dus het tegenovergestelde staat in de lijst verplichte volgordes)
				# dan wisselen we de twee om
				if pages[y]+"|"+pages[x] in orders:
					tmp = pages[y]
					pages[y] = pages[x]
					pages[x] = tmp
					#print(pages[y],"en", pages[x], "omgewisseld tot", pages)

	return pages



def part2():
	global orders
	# Scheidslijn tussen volgordes en manuals is een dubbele regelovergang
	orderstring, manualstring = open(inputFile).read().strip().split("\n\n")
	# Volgordes en manuals omzetten naar lijsten
	orders = orderstring.split("\n")
	manuals = manualstring.split("\n")

	answer = 0
	# Voor alle manuals bepalen we of hij correct is of niet.
	# Is hij niet correct, dan herordenen we de pagina's.
	# Daarna nemen we van deze gecorrigeerde manuals de middelste pagina en tellen hem bij het antwoord op.
	for manual in manuals:
		pages = manual.split(",")
		correct = checkCorrect(pages)
		if not correct:
			newpages = reorder_pages(pages)
			answer += int(newpages[len(newpages)//2])

	print("Part 2:", answer)


if __name__ == "__main__":
	part1()
	part2()