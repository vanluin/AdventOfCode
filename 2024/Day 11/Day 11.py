import functools

inputFile = "input.txt"
inputTestFile = "input-test.txt"

def part1(maxblink):
	line = open(inputFile).read().strip()
	stones = [int(x) for x in line.split(" ")]
	#print(stones)

	workstones = []
	for i in range(maxblink):
		for j,stone in enumerate(stones):
			if stone == 0:
				workstones.append(1)
			elif len(str(stone)) % 2 == 0:
				stoneStr = str(stone)
				stoneLeft, stoneRight = stoneStr[:len(stoneStr)//2], stoneStr[len(stoneStr)//2:]
				workstones.append(int(stoneLeft))
				workstones.append(int(stoneRight))
			else:
				workstones.append(stones[j] * 2024)
		stones = workstones.copy()
		workstones = []
	print("Part 1:", len(stones))

# Deze functie telt het aantal stenen dat de opgegeven steen zal opleveren gegeven dat er nog 'depth' blinks
# mogen worden uitgevoerd.
@functools.cache
def countStones(stone, depth):
	# Als we de maximale diepte bereikt hebben, splitsen we niet verder, en is 1 steen gewoon 1 steen
	if depth == 0:
		return 1

	# Als de steen een 0 is, moeten we weten hoeveel stenen er gaan komen wanner we de steen naar een 1 omzetten, gegeven
	# het aantal keer dat we daarna nog mogen blinken
	elif stone == 0:
		return countStones(1, depth-1)

	# Anders, wanneer de lengte van het getal (als string) even is, dan splitsen en kijken hoeveel stenen elk van de helften
	# zou opleveren, gegeven het aantal keer dat we daarna nog mogen blinken. Die twee aantallen tellen we op en geven we terug.
	elif len(str(stone)) % 2 == 0:
		stoneStr = str(stone)
		stoneLeft, stoneRight = stoneStr[:len(stoneStr) // 2], stoneStr[len(stoneStr) // 2:]
		return countStones(int(stoneLeft), depth-1) + countStones(int(stoneRight), depth-1)

	# en anders kijken hoeveen stenen deze steen oplevert wanneer we hem vermenigvuldigen met 2024, gegeven het aantal
	# keer dat we daarna nog mogen blinken
	else:
		return countStones(stone * 2024, depth-1)


# Deel 2 is niet meer brute-force-baar, dus het moet met recursie en een cache (memoization)
def part2(maxblink):
	line = open(inputFile).read().strip()
	stones = [int(x) for x in line.split(" ")]

	stoneCount = 0
	# Voor elke steen in de input willen we alleen weten hoeveel stenen hij oplevert na 'maxblink' blinks
	# Aangezien de stenen geen invloed op elkaar hebben kunnen we de resultaten van elke steen in de input
	# bij elkaar optellen.
	for stone in stones:
		stoneCount += countStones(stone, maxblink)

	print("Part 2:", stoneCount)

if __name__ == "__main__":
	part1(25)
	part2(75)