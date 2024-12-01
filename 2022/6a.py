inputFile = "d:\\Dropbox\\Python\\AdventOfCode\\6input.txt"
   
with open(inputFile) as f:
    input = ""
    for line in f:
        input += line
    checkLength = 14
    check = input[0:checkLength]
    for i in range(checkLength, len(input)):
        found = True
        for j in range(checkLength):
            if check[j] in check[(j+1):]:
                found = False
                break
        if found:
            print(i, check)
            break
        check = (check+input[i])[1:]
    
        
