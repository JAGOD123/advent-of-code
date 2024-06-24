import logging


def processCards(filepath):
    cards = []
    with open(filepath) as file:
        for card in file:
            raw_arr = card[card.find(":") + 2:].removesuffix("\n").split(" | ")
            raw_arr[0] = [int(i) for i in raw_arr[0].split(" ") if i != ""]
            raw_arr[1] = [int(i) for i in raw_arr[1].split(" ") if i != ""]
            cards.append(raw_arr)
    return cards 

def getWinningPoints(card):
    res = 0
    for winNum in card[0]:
        if winNum in card[1]: 
            if res == 0:
                res = 1
            else:
                res *= 2
    return res

def getWinningCopies(card):
    res = []      
    for winNum in card[0]:
        if winNum in card[1]:
            res.append(winNum)
    return res
    
def getTotalCardsWon():
    cardArr = [1] * len(CARDS)
    logging.debug(cardArr)
    for i in range(len(CARDS)):
        wins = len(getWinningCopies(CARDS[i]))
        logging.debug(f"CARD[{i}] WINS: {wins}")
        for j in range(wins):
            logging.debug(f"i+j+1={i}+{j}+1 = {i+j+1}")
            if i+j+1>192:
                break
            else:
                cardArr[i+j+1] = cardArr[i+j+1] + (cardArr[i])
    return sum(cardArr)

    



logging.basicConfig(level=logging.WARN)

CARDS = processCards("input_4.txt")
winsPoints = [getWinningPoints(card) for card in CARDS]


print(getTotalCardsWon())
        