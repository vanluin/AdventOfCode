import functools

@functools.cache  # 1000x+ speedup
def arrangements(config, group):
    
    # Base cases
    if (len(group) == 0):
        a = int(sum(c == 1 for c in config) == 0)
        return a
    if sum(group) > len(config):
        return 0
    
    # One case for .
    if config[0] == 0:
        a = arrangements(config[1:], group)
        return a

    no1, no2 = 0, 0
    # possibility to start next tile
    if config[0] == 2:
        no2 = arrangements(config[1:], group)

    # possibility to start here
    if all(c != 0 for c in config[:group[0]]) and (config[group[0]] if len(config) > group[0] else 0) != 1:
        no1 = arrangements(config[(group[0] + 1):], group[1:])
    
    return no1 + no2
                

total = 0
with open('input.txt', 'r') as f:
    for line in f:
        
        config, group = line.strip().split(' ')
        
        to_int = {'.': 0, '#': 1, '?': 2}
        config = [to_int[x] for x in config]
        
                
        group = [int(x) for x in group.split(',')]
        
        # ENABLE THIS FOR PART 2
        #config = ((config + [2]) * 5)[:-1]
        #group *= 5
        
        arr = arrangements(tuple(config), tuple(group))
        total += arr

print(total)