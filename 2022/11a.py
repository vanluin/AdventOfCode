group = []

class Monkey:
    global group
    items = []
    operation = ""
    test = ""
    iftrue = -1
    iffalse = -1
    numberOfInspections = 0
    
    def __init__(self, items, operation, test, iftrue, iffalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
    
    def __str__(self):
        return ", ".join([str(i) for i in self.items])
    
    def receive(self, item):
        self.items.append(item)
        
    def throw(self, item, target):
        group[target].receive(item)
        
    def get_operands(self, item, first, second):
        if first == "old":
            left = int(item)
        else:
            left = int(first)
        
        if second == "old":
            right = int(item)
        else:
            right = int(second)
        return left,right
        
    def do_operation(self, item):
        self.numberOfInspections += 1
        
        result = -1
        operation = self.operation.split("=")[1]
        if "*" in operation:
            first, second = operation.split("*")
            left, right = self.get_operands(item, first, second)
            result = left * right
        elif "+" in operation:
            first, second = operation.split("+")
            left, right = self.get_operands(item, first, second)
            result = left + right
            
        return result // 3
    
    def do_test(self, item):
        divisibleBy = int(self.test.split("y")[1])
        return (item % divisibleBy == 0)
        
    def do_turn(self, id):
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.do_operation(item)
            if self.do_test(item):
                self.throw(item, self.iftrue)
            else:
                self.throw(item, self.iffalse)

def printGroup(roundNumber=1):
    global group
    print("Round", str(roundNumber))
    for index, monkey in enumerate(group):
        print("Monkey", index, monkey)
    
    print("\nNumber of inspections")
    for index, monkey in enumerate(group):
        print("Monkey", index, monkey.numberOfInspections)
    
    print("\n")

            
  
with open("11input.txt", "r") as f:
    items = ""
    operation = ""
    test = ""
    iftrue = -1
    iffalse = -1
    for line in f:
        line = line.strip().replace(" ","")
        if line.startswith("Monkey"):
            continue
        elif line.startswith("Starting"):
            items = [int(i) for i in line.split(":")[1].split(",")]
        elif line.startswith("Operation"):
            operation = line.split(":")[1]
        elif line.startswith("Test"):
            test = line.split(":")[1]
        elif line.startswith("Iftrue"):
            iftrue = int(line.split("y")[1])
        elif line.startswith("Iffalse"):
            iffalse = int(line.split("y")[1])
        elif line == "":
            monkey = Monkey(items, operation, test, iftrue, iffalse)
            group.append(monkey)
            items = ""
            operation = ""
            test = ""
            iftrue = -1
            iffalse = -1
                         
    monkey = Monkey(items, operation, test, iftrue, iffalse)
    group.append(monkey)


printGroup()

numRounds = 20

for i in range(numRounds):
    for monkey in group:
        monkey.do_turn(i)
    
printGroup(i+1)

inspectionList = sorted([m.numberOfInspections for m in group])
print(inspectionList[-1]*inspectionList[-2])