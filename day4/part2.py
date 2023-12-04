cards = open("./input.txt", "r").readlines()
stack = []
cardHistory = {}
res = 0


def isWinningCard(card):
    winningNums = set()
    winningCount = i = 0

    while card[i] != ":":
        i += 1

    while card[i] != "|":
        if card[i].isdigit():
            digit = ""
            while card[i].isdigit():
                digit += card[i]
                i += 1
            winningNums.add(digit)
        i += 1
    while i < len(card):
        if card[i].isdigit():
            digit = ""
            while i < len(card) and card[i].isdigit():
                digit += card[i]
                i += 1
            winningCount += 1 if digit in winningNums else 0
        i += 1
    return winningCount


for i, card in enumerate(cards):
    matchingNums = isWinningCard(card)
    res += 1
    matchedArr = []
    for k in range(1, matchingNums + 1):
        stack.append(i + 1 + k)
        matchedArr.append(i + 1 + k)

    cardHistory[i + 1] = matchedArr

while stack:
    cardWon = stack.pop()
    for c in cardHistory[cardWon]:
        stack.append(c)
    res += 1


print(res)
