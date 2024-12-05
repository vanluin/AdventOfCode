inputFile = r"input.txt"

def readInput():
    lines = open(inputFile, "r", encoding="utf-8").read().split("\n\n")
    return lines

seeds = []
seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

def parseLines(lines):
    global seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation
    seeds = lines[0].split(" ")[1:]

    for line in lines[1].split("\n"):
        line = line.strip()
        if not line[0].isdigit():
            continue
        dest, source, length = line.split(" ")
        seedToSoil.append((dest, source, length))
        
    for line in lines[2].split("\n"):
        line = line.strip()
        if not line[0].isdigit():
            continue
        dest, source, length = line.split(" ")
        soilToFertilizer.append((dest, source, length))

    for line in lines[3].split("\n"):
        line = line.strip()
        if not line[0].isdigit():
            continue
        dest, source, length = line.split(" ")
        fertilizerToWater.append((dest, source, length))
        
    for line in lines[4].split("\n"):
        line = line.strip()
        if not line[0].isdigit():
            continue
        dest, source, length = line.split(" ")
        waterToLight.append((dest, source, length))

    for line in lines[5].split("\n"):
        line = line.strip()
        if not line[0].isdigit():
            continue
        dest, source, length = line.split(" ")
        lightToTemperature.append((dest, source, length))
        
    for line in lines[6].split("\n"):
        line = line.strip()
        if not line[0].isdigit():
            continue
        dest, source, length = line.split(" ")
        temperatureToHumidity.append((dest, source, length))
        
    for line in lines[7].split("\n"):
        line = line.strip()
        if len(line) == 0 or not line[0].isdigit():
            continue
        dest, source, length = line.split(" ")

        humidityToLocation.append((dest, source, length))

# Zoek naar 'target' in alle mappings in de mappingList. Komt hij voor, return de gemapte waarde, anders de oorspronkelijke
def findInMapping(target, mappingList):
    result = -1
    for mapping in mappingList:
        dest = int(mapping[0])
        src = int(mapping[1])
        length = int(mapping[2])
        #print("Zoeken naar",target,"tussen",src,"en",src+length-1)
        if target >= src and target < src+length:
            result = dest+(target-src)
            #print("Gevonden:", target, "mapt naar", result)
    
    # Als 'target' niet in de mappinglijst voorkwam, dan is target zelf het resultaat
    if result == -1:
        result = target
        
    return result 

def part1():
    global seeds
    
    locations = []
    for seed in seeds:
        soil = findInMapping(int(seed), seedToSoil)
        fertilizer = findInMapping(soil, soilToFertilizer)
        water = findInMapping(fertilizer, fertilizerToWater)
        light = findInMapping(water, waterToLight)
        temperature = findInMapping(light, lightToTemperature)
        humidity = findInMapping(temperature, temperatureToHumidity)
        location = findInMapping(humidity, humidityToLocation)
        
        locations.append(location)
    
    print("Part 1:", min(locations))
        
def findRanges(targetSets, mappingList):
    entryToCheck = []
    
    setsToDo = targetSets
    while len(setsToDo) > 0:
        currentSet = setsToDo.pop(0)
        #print("Checking", currentSet)
        targetStart = currentSet[0]
        targetEnd = currentSet[1]
 
        foundInMapping = False
        for mapping in mappingList:
            dest = int(mapping[0])
            src = int(mapping[1])
            length = int(mapping[2])
            
            # Als de start in deze mapping valt, dan controleren of end er ook binnen valt. Zo niet, dan splitsen.
            if targetStart >= src and targetStart < src+length:
                #print("targetRange ("+str(targetStart)+","+str(targetEnd)+") valt in mapping ("+str(src)+","+str(src+length)+")")
                if targetEnd > src+length:
                    entryToCheck.append((targetStart, src+length-1))
                    setsToDo.insert(0, (src+length, targetEnd))
                    #print("targetRange ("+str(targetStart)+","+str(targetEnd)+") overschrijdt grens mapping ("+str(src)+","+str(src+length-1)+"), dus ("+str(src+length)+","+str(targetEnd)+") toegevoegd aan setsToDo")
                else:
                    entryToCheck.append((targetStart, targetEnd))
                foundInMapping = True
            # Als de start niet in deze mapping valt, maar de end wel, dan moet er gesplist worden.
            elif targetEnd >= src and targetEnd < src+length:
                #print("begin van range ("+str(targetStart)+","+str(targetEnd)+") valt niet in de mapping ("+str(src)+","+str(src+length)+") maar het einde wel.")
                entryToCheck.append((targetStart, src-1))
                entryToCheck.append((src, targetEnd))
                foundInMapping = True
                
        #De hele target valt niet in een mapping dus gaat ongesplitst mee
        if not foundInMapping:
            #print("Range("+str(targetStart)+","+str(targetEnd)+") valt niet in een mapping")
            entryToCheck.append((targetStart, targetEnd))
        
    return entryToCheck

#Pak de start en eind uit de sourceRange, map beide, en lever op.
#De sourceRange moet hier al opgesplitst zijn binnen de grenzen van mappingList, zodat er geen grens van een mapping overschreden wordt.
def getMappedRange(sourceRange, mappingList):
    result = []
    for (start, end) in sourceRange:
        mappedStart = findInMapping(start, mappingList)
        mappedEnd = findInMapping(end, mappingList)
        result.append((mappedStart, mappedEnd))
    return result

    
def part2():
    global seeds
    locations = []

    # Elke opeenvolging van twee getallen vormt een paar (start, length) van een seednummer en het aantal opvolgende seednummers dat berekend moet worden
    seedSets = []
    for i in range(len(seeds)//2):
        start = int(seeds[2*i])
        length = int(seeds[(2*i)+1])
        seedSets.append((start, start+length))
    print("seedSets", seedSets)

    # Sets nu opknippen in subsets n.a.v. de grenzen binnen de mapping seedToSoil
    seedSetRanges = findRanges(seedSets, seedToSoil)
    # Nu hoogste en laagste waarde van de subsets mappen naar een nieuwe gemapte range
    soilSets = getMappedRange(seedSetRanges, seedToSoil)
    print("soilSets", soilSets)

    # Zelfde truukje voor soilSets: eerst opknippen n.a.v. de grenzen binnen soilToFertilizer
    soilSetRanges = findRanges(soilSets, soilToFertilizer)
    # en dan mappen a.d.h.v. soilToFertilizer mapping
    fertilizerSets = getMappedRange(soilSetRanges, soilToFertilizer)
    print("fertilizerSets", fertilizerSets)

    # Zelfde truukje voor fertilizerSets: opknippen n.a.v. de grenzen binnen fertilizerToWater
    fertilizerSetRanges = findRanges(fertilizerSets, fertilizerToWater)
    # en dan mappen
    waterSets = getMappedRange(fertilizerSetRanges, fertilizerToWater)
    print("waterSets", waterSets)
    
    waterSetRanges = findRanges(waterSets, waterToLight)
    lightSets = getMappedRange(waterSetRanges, waterToLight)
    print("lightSets", lightSets)
    
    lightSetRanges = findRanges(lightSets, lightToTemperature)
    temperatureSets = getMappedRange(lightSetRanges, lightToTemperature)
    print("tempSets", temperatureSets)
    
    temperatureSetRanges = findRanges(temperatureSets, temperatureToHumidity)
    humiditySets = getMappedRange(temperatureSetRanges, temperatureToHumidity)
    print("humiditySets", humiditySets)

    humiditySetRanges = findRanges(humiditySets, humidityToLocation)
    locationSets = getMappedRange(humiditySetRanges, humidityToLocation)
    print("locationSets", locationSets)
    
    print("Part 2:", min([x for (x,y) in locationSets]))
        
lines = readInput()
parseLines(lines)

part1()
#part2()