inputFile = r"input.txt"

def readInput():
    lines = []
    with open(inputFile, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                lines.append(line.strip())
        
    return lines   
    
def part1(lines):
    sum = 0
    for line in lines:
        numbers = list(filter(lambda x: x.isdigit(), line))
        if len(numbers) == 0:
            continue
        sum += int(numbers[0]+numbers[-1])
    print("Part 1:", sum)


def part2(lines):
    sum = 0
    replaces = { "one":"o1e", "two":"t2o", "three":"th3ee", "four":"fo4ur", "five":"fi5ve", "six":"s6x", "seven":"se7en", "eight":"ei8ht", "nine":"ni9ne", "zero":"ze0ro"}
    for line in lines:
        tmpline = ""
        for character in line:
            tmpline += character
            for key in replaces.keys():
                if key in tmpline:
                    tmpline = tmpline.replace(key, replaces[key])
        numbers = list(filter(lambda x: x.isdigit(), tmpline))
        if len(numbers) == 0:
            continue
        sum += int(numbers[0]+numbers[-1])
    print("Part 2:", sum)

lines = readInput()
part1(lines)
part2(lines)