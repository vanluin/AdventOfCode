from functools import reduce
inputFile = r"input.txt"

def readInput():
    lines = open(inputFile, "r", encoding="utf-8").read().split("\n")
    return lines

def getDistanceForTime(time, maxtime):
    if time > maxtime or time < 0:
        return 0
    else:
        return time * (maxtime-time)

def part1(lines):
    # Lijstje maken van alle tijden en afstanden, en checken dat het aantal getallen in beide lijsten gelijk is.
    times = [int(x.strip()) for x in lines[0].replace("Time:", "").split(" ") if x.strip() != ""]
    distances = [int(x.strip()) for x in lines[1].replace("Distance:", "").split(" ") if x.strip() != ""]
    assert len(times) == len(distances), f"aantal in times ({times}) ongelijk aan aantal in distances ({distances})"
    
    # Maak een lijst van lijsten van tuples. Elke tuple is (racenummer, indruktijd) voor een winnende race. De resultaten zijn gegroepeerd per race.
    winningOptions = [[(y+1, x) for x in range(0, times[y]) if getDistanceForTime(x, times[y]) > distances[y]] for y in range(0, len(times)) ]
    #print(winningOptions)
    
    # De score berekenen door alle lengtes van de sublijsten per race met elkaar te vermenigvuldigen
    score = reduce(lambda x, y: x * y, [len(x) for x in winningOptions])
    print("Part 1:", score)

def part2(lines):
    # Alle tekens achter Time en Distance samenvoegen tot geheel getal
    time = int(lines[0].replace("Time:", "").replace(" ","").strip())
    distance = int(lines[1].replace("Distance:", "").replace(" ","").strip())
    
    # En nu de hele range van 0 tot "time" aflopen en alle winnende versies opslaan
    winningOptions = [x for x in range(0, time) if getDistanceForTime(x, time) > distance]
    print("Part 2:", len(winningOptions))
    
    

lines = readInput()
part1(lines)
part2(lines)