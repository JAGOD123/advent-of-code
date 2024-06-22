import re
def getNumbers():
    '''

    '''
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    arr = []
    with open("input_1.txt") as file:
        for line in file:
            format_line = replace_full_words_with_num(line)
            first_num = last_num = None
            for char in format_line:
                if char in nums:
                    if first_num == None:
                        first_num = char
                    else:
                        last_num = char
            arr.append(int(first_num + first_num)) if last_num == None else arr.append(int(first_num + last_num))            
    return sum(arr)

def replace_full_words_with_num(line):
    '''
        Replaces the middle letter of the word with the right number.
        Replace the middle letter to ensure that words that overlap format correctly
        So 'fiveight' becomes 58 not '5ight' if i were to replace the whole word
    '''
    word_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(word_nums)):
        res = [i.start() for i in re.finditer(word_nums[i], line)] 
        for index in res:
            length = round(len(word_nums[i]) / 2) -1 
            char_loc = index + length
            line = line[:char_loc] + str(i+1) + line[char_loc+1:]
    return line

print(getNumbers())