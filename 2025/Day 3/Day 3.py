TEST = False

if TEST:
  inputFile = r"/content/drive/MyDrive/AdventOfCode/Day 3/input-test.txt"
else:
  inputFile = r"/content/drive/MyDrive/AdventOfCode/Day 3/input.txt"


def part1():
  with open(inputFile) as f:
    lines = [x.strip() for x in f.readlines()]

  joltages = []
  # Per regel batterijen: vindt het hoogste getal dat niet het laatste getal is,
  # en daarna het hoogste getal erachter. Plak aan elkaar en bewaar.
  for line in lines:
    maxDigit = max([int(x) for x in line[:-1]])
    locDigit = line.index(str(maxDigit))
    nextMax = max([int(x) for x in line[locDigit+1:]])
    joltages.append(int(str(maxDigit)+str(nextMax)))

  # Het antwoord is de som van alle bewaarde joltages.
  print("Part 1:", sum(joltages))


def part2():
  with open(inputFile) as f:
    lines = [x.strip() for x in f.readlines()]

  joltages = []
  # Per regel batterijen: zoek steeds het hoogste getal dat je kunt vinden wanneer
  # je elk cijfer een keer weglaat, net zolang tot je 12 cijfers hebt.
  # Bewaar dat getal.
  for line in lines:
    while len(line) > 12:
      targets = [line[:x]+line[x+1:] for x in range(0, len(line))]
      line = str(max(targets))
    joltages.append(int(line))

  # Het antwoord is weer de som van alle bewaarde getallen.
  print("Part 2:", sum(joltages))


if __name__ == "__main__":
  part1()
  part2()