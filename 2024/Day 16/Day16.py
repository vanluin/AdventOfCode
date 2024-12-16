
inputFile = "input.txt"
inputTestFile = "input-test.txt"

def part1():
    grid = [x.strip() for x in open(inputTestFile).read().split("\n")]
    start = [(row,col, '>') for row,line in enumerate(grid) for col,point in enumerate(grid[row]) if grid[row][col] == 'S'][0]
    end = [(row,col) for row,line in enumerate(grid) for col,point in enumerate(grid[row]) if grid[row][col] == 'E'][0]
    walls = [(row,col) for row,line in enumerate(grid) for col,point in enumerate(grid[row]) if grid[row][col] == '#']
    print(start, end)
    routes = []
    visited = []



def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()