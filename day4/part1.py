cards = open("./input.txt", "r").readlines()
res = 0

for card in cards:
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

    res += 2 ** (winningCount - 1) if winningCount > 1 else winningCount
print(res)
