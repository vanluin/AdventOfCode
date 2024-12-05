inputFile = r"input.txt"

def readInput():
    lines = []
    with open(inputFile, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                lines.append(line.strip())
    return lines

#which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
def part1(lines):
    result = 0
    for line in lines:
        gameid, setString = line.split(":")
        gameid = int(gameid.replace("Game ", ""))
        sets = setString.split(";")

        maxes = {}
        maxes['red'] = maxes['blue'] = maxes['green'] = 0
        for set in sets:
            balls = set.split(",")
            for ball in balls:
                ball = ball.strip()
                amount, colour = ball.split(" ")
                if int(amount) > maxes[colour]:
                    maxes[colour] = int(amount)
                    
        if maxes['red'] <= 12 and maxes['green'] <= 13 and maxes['blue'] <= 14:
            result += gameid
            
    print("Part 1:", result)

#what is the fewest number of cubes of each color that could have been in the bag to make the game possible
def part2(lines):
    result = 0
    for line in lines:
        gameid, setString = line.split(":")
        gameid = int(gameid.replace("Game ", ""))
        sets = setString.split(";")
        
        maxes = {}
        maxes['red'] = maxes['blue'] = maxes['green'] = 0
        for set in sets:
            balls = set.split(",")
            for ball in balls:
                ball = ball.strip()
                amount, colour = ball.split(" ")
                if int(amount) > maxes[colour]:
                    maxes[colour] = int(amount)
                    
        power = maxes['red'] * maxes['green'] * maxes['blue']
        result += power
    
    print("Part 2:", result)

lines = readInput()
part1(lines)
part2(lines)