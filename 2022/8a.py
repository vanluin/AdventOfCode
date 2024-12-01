trees = []
with open("c:\\temp\\8input.txt", "r") as f:
    for line in f:
        trees.append(list(line.strip()))

height = len(trees)
width = len(trees[0])

num_visible = 0

def check_up(y, x):
    global trees
    global height
    global width
    
    target_height = trees[y][x]
    
    is_visible = True
    for i in range(y):
        if trees[i][x] >= target_height:
            is_visible = False
            
    return is_visible

def check_down(y, x):
    global trees
    global height
    global width
    
    target_height = trees[y][x]
    
    is_visible = True
    for i in range(y+1, height):
        if trees[i][x] >= target_height:
            is_visible = False
            
    return is_visible

def check_left(y, x):
    global trees
    global height
    global width
    
    target_height = trees[y][x]
    
    is_visible = True
    for i in range(x):
        if trees[y][i] >= target_height:
            is_visible = False
            
    return is_visible

def check_right(y, x):
    global trees
    global height
    global width
    
    target_height = trees[y][x]
    
    is_visible = True
    for i in range(x+1, width):
        if trees[y][i] >= target_height:
            is_visible = False
            
    return is_visible
    
num_visible = 0
for y in range(height):
    for x in range(width):
        if x == 0 or y == 0 or x == width-1 or y == height-1:
            is_visible = True
        else:
            is_visible = check_up(y, x) or check_down(y, x) or check_left(y, x) or check_right(y, x)
            
        #print(y, x, trees[y][x], is_visible)
        if is_visible:
            num_visible += 1
            
print(num_visible)
    