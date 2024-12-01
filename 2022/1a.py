
inputFile = "1input.txt"

elves = []

numberElf = 0
elves.append(0)

with open(inputFile) as f:
    for line in f:
        if line.strip() == '':
            numberElf += 1
            elves.append(0)
        else:
            elves[numberElf] += int(line.strip())
            
for elf in sorted(elves):
    print(elf)
    
print("Max:", max(elves))

elvesSorted = sorted(elves)
last = len(elvesSorted)-1

print("Top 3:", elvesSorted[last],elvesSorted[last-1], elvesSorted[last-2], (elvesSorted[last] + elvesSorted[last-1] + elvesSorted[last-2]))

    

    