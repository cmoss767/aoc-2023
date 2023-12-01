file = open("input.txt", "r").read().split()


sum = 0
print(file)

for line in file:
    first, firstNum, lastNum = False, '', ''

    for i, c in enumerate(line):
        if not first and c.isdigit():
            firstNum = c
            first = True
        elif c.isdigit():
            lastNum = c

    if not lastNum:
        sum += int(firstNum + firstNum)
    else:
        sum += int(firstNum + lastNum)


print(sum)
