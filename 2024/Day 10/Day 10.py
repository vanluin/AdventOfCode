
inputFile = "input.txt"
inputTestFile = "input-test.txt"


def is_reachable(grid, top, currentposition):
	x,y = currentposition

	# Als we de top hebben bereikt, dan zijn we klaar en is de top bereikbaar
	if x == top[0] and y == top[1]:
		return True

	# Is de top nog niet bereikt, dan bepalen we de huidige hoogte, en kijken voor de vier richtingen
	# of die stap nog binnen het grid ligt, en zo ja, of die waarde exact 1 hoger is dan de huidige.
	# Is dat zo, dan kijken we of vanaf dat nieuwe punt de gevraagde top bereikbaar is.
	value = grid[x][y]
	for (dx, dy) in [(-1,0), (0,1), (1,0), (0,-1)]:
		if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]):
			if grid[x+dx][y+dy] == value + 1:
				if is_reachable(grid, top, (x+dx,y+dy)):
					return True

	# Hier aangekomen is er geen omliggend punt dat hoger is dan het huidige terwijl we niet op de gevraagde top zijn.
	return False


def part1():
	# Inlezen van het bestand als een lijst van per regel een lijst van getallen.
	grid = [[int(char) for char in line.strip()] for line in open(inputFile).read().split("\n")]
	# Alle tops en alle starts bepalen
	tops = [(row,col) for row,line in enumerate(grid) for col,point in enumerate(grid[row]) if grid[row][col] == 9]
	starts = [(row,col) for row,line in enumerate(grid) for col,point in enumerate(grid[row]) if grid[row][col] == 0]

	totalscore = 0
	for start in starts:
		score = 0
		for top in tops:
			# Als de top bereikbaar is vanaf de start, dan telt deze combinatie mee voor de trailheadscore van deze start
			if is_reachable(grid, top, start):
				score += 1

		print("Startpositie", start, "heeft score", score)
		totalscore += score

	print("Part 1", totalscore)





def part2():
	pass

if __name__ == "__main__":
	part1()
	part2()