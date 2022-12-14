pairs = []
inputFile = "d:\\Coding\\AdventOfCode\\4input.txt"

def expandRange(sections):
    result = []
    begin,end = [int(i) for i in sections.split("-")]
    for i in range(begin, end+1):
        result.append(i)
    return result

# checks if the first list is fully contained in the second
def fullyContains(first, second):
    for item in first:
        if item not in second:
            return False
    # if we reached the end of 'first' without returning False, return True
    return True
    

with open(inputFile) as f:
    group = []
    for line in f:
        line = line.strip()
        pair = line.split(",")
        pairs.append([expandRange(pair[0]),expandRange(pair[1])])

count = 0
for pair in pairs:
    if fullyContains(pair[0], pair[1]) or fullyContains(pair[1], pair[0]):
        count += 1
        
print(count)