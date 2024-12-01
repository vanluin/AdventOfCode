pairs = []
inputFile = "d:\\Coding\\AdventOfCode\\4input.txt"

def expandRange(sections):
    result = []
    begin,end = [int(i) for i in sections.split("-")]
    for i in range(begin, end+1):
        result.append(i)
    return result

# checks if the first list is fully contained in the second
def partiallyContains(first, second):
    for item in first:
        if item in second:
            return True
    return False
    

with open(inputFile) as f:
    group = []
    for line in f:
        line = line.strip()
        pair = line.split(",")
        pairs.append([expandRange(pair[0]),expandRange(pair[1])])

count = 0
for pair in pairs:
    if partiallyContains(pair[0], pair[1]):
        count += 1
        
print(count)