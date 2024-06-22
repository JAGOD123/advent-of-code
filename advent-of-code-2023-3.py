def process_file(filepath):
    arr = []
    with open(filepath) as file:
        for line in file:
            line_arr = []
            for c in line:
                if c == "\n":
                    continue
                line_arr.append(c)
            arr.append(line_arr)
    return arr


def find_part_number(schematic):
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    arr_nums = []
    line = 129 
    for line in range(len(schematic)):
        c_index = 0 
        while c_index < len(schematic[line]):
            #print(f"                     c_index: {c_index}")
            if schematic[line][c_index] in nums:
                #print("Line ", line)
                #print("pos  ", c_index)
                #print("item ", schematic[line][c_index])
                #print("\n")
            

                if isSymbolAdjecent(schematic, line, c_index):
                    # fit in if were starting at 0 or ending falls over
                    pos = c_index
                    numStr = ""
                    pointerMoved = 0
                    while schematic[line][pos-1] in nums and pos-1 >= 0: 
                        pos -= 1 
                        pointerMoved -= 1
                    while pos+1 < 140 and schematic[line][pos+1] in nums:
                        numStr += schematic[line][pos]
                        pos += 1
                        pointerMoved +=1 
                    numStr += schematic[line][pos]
                    #print(f"            POINTERMOVED: {pointerMoved}")
                    #print(f"LINE: {str(line)} C_INDEX:  {c_index}   NUMSTR " + numStr)
                    c_index += pointerMoved
                    arr_nums.append(int(numStr))
            c_index += 1 
    #print(arr_nums)
    return arr_nums


def isSymbolAdjecent(schematic, lineNum, index):
    ## need to check -1 line -1 index
    symbols = ["*", "%", "-", "#", "*", "=", "/", "+", "@", "$", "&"]
    checks = [None, None, None,
              None,       None,
              None, None, None]
    if lineNum-1 < 0:
        checks[0] = 'e'
        checks[1] = 'e'
        checks[2] = 'e'
    if lineNum+1 >= len(schematic):
        checks[5] = 'e'
        checks[6] = 'e'
        checks[7] = 'e'
    if index-1 < 0:
        checks[0] = 'e'
        checks[3] = 'e'
        checks[5] = 'e'
    if index+1 >= len(schematic[lineNum]):
        checks[2] = 'e'
        checks[4] = 'e'
        checks[7] = 'e'
    for i in range(len(checks)):
        if checks[i] == None:
            match i:
                case 0:
                    checks[0] = schematic[lineNum-1][index-1]
                case 1: 
                    checks[1] = schematic[lineNum-1][index]
                case 2:
                    checks[2] = schematic[lineNum-1][index+1]
                case 3: 
                    checks[3] = schematic[lineNum][index-1]
                case 4: 
                    checks[4] = schematic[lineNum][index+1]
                case 5:
                    checks[5] = schematic[lineNum+1][index-1]
                case 6: 
                    checks[6] = schematic[lineNum+1][index]
                case 7: 
                    checks[7] = schematic[lineNum+1][index+1]
         
    for char in checks:
        if char in symbols:
            return True 
    return False

schematic = process_file("input_3.txt")
print(sum(find_part_number(schematic)))

