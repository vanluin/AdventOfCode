TEST = False

if TEST:
    inputFile = r"input-test.txt"
else:
    inputFile = r"input.txt"


def isInList(product, freshList):
    for fresh in freshList:
        low, high = fresh.split("-")
        if int(product) >= int(low) and int(product) <= int(high):
            return True
    return False


def part1():
    with open(inputFile) as f:
        freshList, productList = f.read().split("\n\n")
        freshList = [x.strip() for x in freshList.split("\n")]
        productList = [x.strip() for x in productList.split("\n")]

    amountFresh = 0
    for product in productList:
        if product.strip() != "" and isInList(product, freshList):
            amountFresh += 1

    print("Part 1:", amountFresh)


def part2():
    with open(inputFile) as f:
        freshList, productList = f.read().split("\n\n")
        freshList = [x.strip() for x in freshList.split("\n")]

    sortedList = sorted(freshList, key=lambda fresh: int(fresh.split("-")[0]))
    changed = True
    while changed:
        changed = False
        for i, part in enumerate(sortedList):
            if i == 0:
                continue
            low, high = part.split("-")
            prevLow, prevHigh = sortedList[i-1].split("-")
            if int(low) <= int(prevHigh):
                sortedList[i-1] = prevLow+"-"+str(max(int(high), int(prevHigh)))
                sortedList.pop(i)
                changed = True

    totalFresh = 0
    for items in sortedList:
        low, high = items.split("-")
        totalFresh += int(high) - int(low) + 1

    print("Part 2:", totalFresh)


if __name__ == "__main__":
    part1()
    part2()
