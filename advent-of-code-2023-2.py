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
                
def minimum_cubes(game_arr_dict):
    # list of list of dicts, for each game get the buggest numberfor each column
    power_arr = []
    for game in game_arr_dict:
        d = {"red": 0, "green": 0, "blue": 0}
        for d_n in game:
            if d.get("red") < d_n.get("red"):
                d["red"] = d_n.get("red")
            if d.get("green") < d_n.get("green"):
                d["green"] = d_n.get("green")
            if d.get("blue") < d_n.get("blue"):
                d["blue"] = d_n.get("blue")

        print(d)
        num = 1
        for colour, val in d.items():
            if val == 0: 
                continue
            num *= val
        print(num)
        power_arr.append(num)
    return power_arr
            


file = process_file("input_2.txt")
games = vaild_games(file)
print(sum(games))

minimum_arr = minimum_cubes(file)
print(sum(minimum_arr))


