inputFile = r"input.txt"

def readInput():
    lines = open(inputFile, "r", encoding="utf-8").read().split("\n\n")
    return lines

def checkMirrored(line):
    l = len(line)
    #print(l, line, line[:(l//2)], line[::-1][:(l//2)] )
    return line[:(l//2)] == line[::-1][:(l//2)]
    

def checkField(lines):
    isMirrored = True
    for line in lines:
        isMirrored = isMirrored & checkMirrored(line)
        if not isMirrored:
            break
    return isMirrored

def part1(lines):
    horizontals = 0
    verticals = 0
    for index, field in enumerate(lines):
        # Eerst horizontaal checken
        # Bij een even aantal posities nemen we het hele veld
        lines = [x.strip() for x in field.split("\n")]
        direction = ""
        middle = 0
        if len(lines) % 2 == 0:
            isMirrored = checkField(lines)
            if isMirrored:
                direction = "horizontal"
                middle = (len(lines) // 2)
                print("h1", direction, middle)
                horizontals += middle
        else:
        # Bij een oneven aantal posities checken we eerst het weglaten van
        # de eerste kolom
            sublines = [x[1:] for x in lines]
            isMirrored = checkField(sublines)
            if isMirrored:
                direction = "horizontal"
                middle = (len(sublines) // 2) + 1
                print("h2", direction, middle)
                horizontals += middle
            else:
            # En als dat niet gespiegeld is, het weglaten van de laatste kolom
                sublines = [x[:-1] for x in lines]
                isMirrored = checkField(sublines)
                if isMirrored:
                    direction = "horizontal"
                    middle = (len(sublines) / 2) - 1
                    print("h3",direction, middle)
                    horizontals += middle
        
        # Als we geen spiegeling aangetroffen hebben, checken we verticaal
        if direction == "":
            # Het veld kantelen, zodat rijen kolommen worden
            lines = ["".join([line[i] for line in field.split("\n")]) for i in range(len(field.split("\n")))]
            direction = ""
            middle = 0
            if len(lines) % 2 == 0:
                isMirrored = checkField(lines)
                if isMirrored:
                    direction = "vertical"
                    middle = (len(lines) // 2) + 1
                    print("v1", direction, middle)
                    verticals += middle
            else:
            # Bij een oneven aantal posities checken we eerst het weglaten van
            # de eerste kolom
                sublines = [x[1:] for x in lines]
                isMirrored = checkField(sublines)
                if isMirrored:
                    direction = "vertical"
                    middle = (len(sublines) // 2) + 2
                    print("v2", direction, middle)
                    verticals += middle
                else:
                # En als dat niet gespiegeld is, het weglaten van de laatste kolom
                    sublines = [x[:-1] for x in lines]
                    isMirrored = checkField(sublines)
                    if isMirrored:
                        direction = "vertical"
                        middle = (len(sublines) / 2)
                        print("v3",direction, middle)
                        verticals += middle
            
        print("Part 1", verticals + (100 * horizontals))
        
        
def part2(lines):
    pass
           


lines=readInput()
part1(lines)
part2(lines)
