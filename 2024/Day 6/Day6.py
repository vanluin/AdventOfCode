
inputFile = "input.txt"
inputTestFile = "input-test.txt"


def part1():
	# Inlezen van het inputbestand, maken van een lijst obstacles en bepalen van de startpositie en boundaries
	field = [x.strip() for x in open(inputFile, "r").read().split("\n")]
	obstacles = [(row, col) for row,line in enumerate(field) for col,obstacle in enumerate(line) if obstacle == "#"]
	startpos = [(row, col) for row,line in enumerate(field) for col,obstacle in enumerate(line) if obstacle == "^"][0]
	max_row = len(field)
	max_col = len(field[0])
	# De richtingen waarin we kunnen lopen, steeds rechtsaf van de vorige
	directions = [(-1,0), (0,1), (1,0), (0,-1)]
	# We starten kijkend naar boven, dus index 0 van directions
	current_dir_index = 0

	# de startpositie is uiteraard bezocht
	visited = [startpos]
	currentpos = startpos
	# Zolang we binnen de boundaries van het veld zitten blijven we herhalen
	while (0 <= currentpos[0] < max_row) and (0 <= currentpos[1] < max_col):
		# Vul een testpositie met de waarde van de huidige positie + de offset van de richting
		direction = directions[current_dir_index]
		testpos = tuple(a+b for a,b in zip(currentpos, direction))

		# Kijk dan of we op de testpositie een obstakel tegenkomen. Zo ja, kijk dan rechtsaf en test opnieuw
		while testpos in obstacles:
			current_dir_index = (current_dir_index + 1) % 4
			direction = directions[current_dir_index]
			testpos = tuple(a + b for a, b in zip(currentpos, direction))

		# Dat we hier komen betekent dat we verplaatst zijn, dus onze huidige positie aanpassen en de nieuwe locatie
		# toevoegen aan de lijst bezochte punten
		currentpos = testpos
		visited.append(currentpos)

	# Printen van het resultaat als set (dus zonder dubbelen) - 1 (want die eerste buiten het veld moet eraf)
	print("Part 1", len(set(visited))-1)
	# Teruggeven van de afgelegde route ivm deel 2
	return visited


def part2(orig_route):
	# Inlezen van het inputbestand, maken van een lijst obstacles en bepalen van de startpositie en boundaries
	field = [x.strip() for x in open(inputFile, "r").read().split("\n")]
	obstacles = [(row, col) for row,line in enumerate(field) for col,obstacle in enumerate(line) if obstacle == "#"]
	startpos = [(row, col) for row,line in enumerate(field) for col,obstacle in enumerate(line) if obstacle == "^"][0]
	max_row = len(field)
	max_col = len(field[0])
	# De richtingen waarin we kunnen lopen, steeds rechtsaf van de vorige
	directions = [(-1,0), (0,1), (1,0), (0,-1)]
	# We starten kijkend naar boven, dus index 0 van directions
	current_dir_index = 0

	# Alleen punten op de orignele route hoeven getest te worden
	points_to_test = set(orig_route)

	cycles = 0
	# Voor alle punten in de originele route kijken we of een blokkade op deze route tot een cycle leidt.
	for point_to_test in points_to_test:
		currentpos = startpos
		current_dir_index = 0
		# Naast de positie nu ook de richting in visited opslaan, omdat een cycle alleen een cycle is
		# wanneer naast de positie ook de richting dezelfde als eerder is
		visited = [(currentpos, current_dir_index)]
		cycle_found = False

		# Herhaal zolang we nog op het veld zitten...
		while (0 <= currentpos[0] < max_row) and (0 <= currentpos[1] < max_col):
			# Vul een testpositie met de waarde van de huidige positie + de offset van de richting
			direction = directions[current_dir_index]
			testpos = tuple(a+b for a,b in zip(currentpos, direction))

			# Kijk dan of we op de testpositie een oorspronkelijk obstakel of het nieuwe obstakel tegenkomen
			# Zo ja, kijk dan rechtsaf en test opnieuw
			while testpos in obstacles+[point_to_test]:
				current_dir_index = (current_dir_index + 1) % 4
				direction = directions[current_dir_index]
				testpos = tuple(a + b for a, b in zip(currentpos, direction))

			# Dat we hier komen betekent dat we verplaatst zijn, dus onze huidige positie aanpassen
			currentpos = testpos

			# Als de combinatie van positie en richting al eerder is bezocht hebben we een cycle
			# en stoppen we de while lus
			if (currentpos, current_dir_index) in visited:
				cycle_found = True
				break
			else:
				# en zo niet, dan voegen we positie+richting toe aan de lijst bezochte punten
				visited.append((testpos, current_dir_index))

		if cycle_found:
			cycles += 1
			#print("Cycle", cycles, "gevonden")

	print("Part 2:", cycles)

if __name__ == "__main__":
	orig_route = part1()
	part2(orig_route)