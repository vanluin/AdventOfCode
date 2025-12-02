
TEST = False

if TEST:
    inputFile = "input-test.txt"
else:
    inputFile = "input.txt"


def part1():
    curPos = 50
    amountZero = 0
    with open(inputFile) as f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:
            direction, amount = line[0],int(line[1:])
            if direction == "L":
                amount = -amount
            curPos = (curPos + amount) % 100
            if curPos == 0:
                amountZero += 1

    print("Part 1:", amountZero)



def part2():
    curPos = 50
    amountZero = 0
    with open(inputFile) as f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:
            direction, amount = line[0],int(line[1:])
            dPos = 1
            if direction == "L":
                dPos = -1
            for i in range(amount):
                curPos = (curPos + dPos) % 100
                if curPos == 0:
                    amountZero += 1

    print("Part 2:", amountZero)


if __name__ == "__main__":
    part1()
    part2()
