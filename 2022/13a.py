import ast

pairs = []
correctOrder = []

def checkList(left, right):
    print("Entering checkList with:", left, type(left), right, type(right))
    
    result = True
    for i in range(len(left)):
        print("i", i)
        if isinstance(left[i], list) or isinstance(right[i], list):
            if not isinstance(left[i], list):
                left[i] = [left[i]]
            if not isinstance(right[i], list):
                right = [right[i]]
                
            result = result and checkList(left[i], right[i])
        else:
            result = result and left[i] <= right[i]
            
    return result
    
def checkOrder():
    
    global pairs
    global correctOrder
    
    for index, pair in enumerate(pairs):
        print("---", index+1)
        left, right = pair
        leftList = ast.literal_eval(left)
        print("Left:", leftList, type(leftList))
        rightList = ast.literal_eval(right)
        print("Right:", rightList, type(rightList))
        
        
        correct = checkList(leftList, rightList)
        correctOrder.append(correct)
            
        if index == 1:
            break
        
        
        
    

with open("13testinput.txt", "r") as f:
    pair = []
    for line in f:
        if line.strip() == "":
            pairs.append(pair)
            pair = []
        else:
            pair.append(line.strip())

    pairs.append(pair)
    pair = []


checkOrder()

for index,check in enumerate(correctOrder):
    print(index+1, check)