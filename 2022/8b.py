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
    
    num_visible = 0
    for i in reversed(range(y)):
        #if trees[i][x] <= target_height:
        num_visible += 1
        if trees[i][x] >= target_height:        
            break
            
    return num_visible

def check_down(y, x):
    global trees
    global height
    global width
    
    target_height = trees[y][x]
    
    num_visible = 0
    for i in range(y+1, height):
#        if trees[i][x] <= target_height:
        num_visible += 1
        if trees[i][x] >= target_height:
            break
            
    return num_visible

def check_left(y, x):
    global trees
    global height
    global width
    
    target_height = trees[y][x]
    
    num_visible = 0
    for i in reversed(range(x)):
#        if trees[y][i] <= target_height:
        num_visible += 1
        if trees[y][i] >= target_height:
            break          
    return num_visible

def check_right(y, x):
    global trees
    global height
    global width
    
    target_height = trees[y][x]
    
    num_visible = 0
    for i in range(x+1, width):
#        print(i, trees[y][i], target_height)
#        if trees[y][i] <= target_height:
        num_visible += 1
#        print("#",i, trees[y][i], target_height)
        if trees[y][i] >= target_height:
            break          
    return num_visible
    
high_score = 0
for y in range(height):
    for x in range(width):
        up = check_up(y,x)
        down = check_down(y,x)
        left = check_left(y,x)
        right = check_right(y,x)
        
        this_score = up * down * left * right
        if this_score > high_score:
            high_score = this_score
            
print(high_score)

        
#y = 1
#x = 1
#print(y, x, trees[y][x], check_left(y, x))
 
#y = 3
#x = 2

#up = check_up(y,x)
#down = check_down(y,x)
#left = check_left(y,x)
#right = check_right(y,x)
            
#print(y, x, trees[y][x], up)
#print(y, x, trees[y][x], left)
#print(y, x, trees[y][x], down)
#print(y, x, trees[y][x], right)

#print(up * down * left * right)
    