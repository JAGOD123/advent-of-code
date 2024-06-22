# iterate through the lines and see what games have too many cubes of eahc colour


def process_file(filePath):
    # takes in file path and returns a array? of each game and hiow many red gree or blue xcubes were pulled out
    game_arr = []

    with open(filePath) as file:
        for game in file: 
            raw_arr = game[game.find(":") + 2:].removesuffix("\n").split("; ")
            r_arr = []
            for round in raw_arr:
                round_arr = round.split(", ")

                d = {"red": 0, "green": 0, "blue": 0}
                for go in round_arr:
                    index = go.find(" ")
                    num = go[:index]
                    colour = go[index+1:]
                    d[colour] = int(num)
                r_arr.append(d)
            game_arr.append(r_arr)
    return game_arr

def vaild_games(game_arr_dict):
    game_arr = []
    for i in range(len(game_arr_dict)):
        vaild = True
        for d in game_arr_dict[i]:
            vaild
            if d.get("red") > 12 or d.get("green") > 13 or d.get("blue") > 14:
                vaild = False
        if vaild:
            game_arr.append(i+1)
            
    return game_arr
                



file = process_file("input_2.txt")
games = vaild_games(file)
print(sum(games))


