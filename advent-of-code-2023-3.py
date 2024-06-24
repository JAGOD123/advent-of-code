import logging
NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
SYMBOLS = ["*", "%", "-", "#", "*", "=", "/", "+", "@", "$", "&"]

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
    arr_nums = []
    for line in range(len(schematic)):
        c_index = 0 
        while c_index < len(schematic[line]):
            #print(f"                     c_index: {c_index}")
            if schematic[line][c_index] in NUMS:         
                if isSymbolAdjecent(schematic, line, c_index):
                    num, pos = getFullNumAndPos(schematic, line, c_index) 
                    c_index += pos
                    arr_nums.append(num)
            c_index += 1 
    #print(arr_nums)
    return arr_nums

def getSurronding(schematic, lineNum, index):
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
    return checks

def getFullNumAndPos(schematic, lineNum, index):
    numStr = ""
    pointerMoved = 0
    while schematic[lineNum][index-1] in NUMS and index-1 >= 0: 
        index -= 1 
        pointerMoved -= 1
    while index+1 < len(schematic[lineNum]) and schematic[lineNum][index+1] in NUMS:
        numStr += schematic[lineNum][index]
        index += 1
        pointerMoved +=1 
    numStr += schematic[lineNum][index]

    return int(numStr), pointerMoved


def isSymbolAdjecent(schematic, lineNum, index):
    checks = getSurronding(schematic, lineNum, index)
    for char in checks:
        if char in SYMBOLS:
            return True 
    return False

def is_gear(schematic):
    # check that the numbers are 
    logging.warning("Starting isGear")
    gearRatios = []
    
    for line in range(len(schematic)):
        
        c_index = 0 
        while c_index < len(schematic[line]):
            if c_index > 140:
                break
            if schematic[line][c_index] == "*":
                logging.warning("\n\n")
                logging.warning(f"Got Gear at: {line}:{c_index}")
                surr = getSurronding(schematic, line, c_index)
                print(surr)
                gearNums = []
                i = 0 
                while i < len(surr):
                    
                    if surr[i] in NUMS:
                        temp_index = c_index
                        temp_line = line 
                        match i:
                            case 0:
                                temp_index += -1
                                temp_line  += -1 
                            case 1: 
                                temp_line  += -1
                            case 2:
                                temp_index +=  1
                                temp_line  += -1 
                            case 3: 
                                temp_index += -1
                            case 4: 
                                temp_index +=  1
                            case 5:
                                temp_index += -1
                                temp_line  +=  1 
                            case 6: 
                                temp_line  +=  1 
                            case 7: 
                                temp_index +=  1
                                temp_line  +=  1 
                        
                        num, pointer = getFullNumAndPos(schematic, temp_line, temp_index)
                        logging.warning(f"Num {num} at surr index {i}")
                        logging.warning(f"Pointer is adding {pointer}")
                        gearNums.append(num)
                        print(gearNums)
                        # if the pointer is positive that we havent started at the end of the number
                        # so if at index 0 and pointer returns 2, that means the full word is 0,1,2
                        # so if the cuur index while looking at 1,2,3 becomes > 3 skip to 4
                        # same for 7,8,9 but end 

                        if pointer == 0:
                            if i == 0: 
                                i = 2
                            elif i < 3:
                                i = 3 
                            elif i == 3:
                                i = 4
                            elif i == 4:
                                #impossile
                                i = None
                            elif i == 5:
                                i = 7
                            elif i > 5:
                                break
                        elif pointer == 2 and i == 4:
                            i = 5
                        elif i < 3:
                            i = 3 
                        else:
                            break
                            




                        #if i <= 2 and i + pointer >= 2:
                        #    i = 3
                        #elif i >=5 and i <= 8 and i+ pointer >=8:
                        #    break
                        #else:
                        #    i += 1
                    else:
                        i += 1 
                
                if len(gearNums) == 2:
                    gearRatios.append(gearNums[0]*gearNums[1])
            c_index += 1 
    print(gearRatios)
    return gearRatios
    



schematic = process_file("input_3.txt")
#print(sum(find_part_number(schematic)))



print(sum(is_gear(schematic)))

