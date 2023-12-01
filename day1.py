

file = open("input.txt", "r").read().split()


charToDigit = {"one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
sum = 0


for line in file:
    lines = []
    for num in charToDigit.keys():
        lines.append(line.replace(num, charToDigit[num]))
    line = min(lines)

    first, firstNum, lastNum = False, '', ''

    for char in line:
        if not first and char.isdigit():
            firstNum = char
            first = True
        elif char.isdigit():
            lastNum = char

    if not lastNum:
        sum += int(firstNum + firstNum)
    else:
        sum += int(firstNum + lastNum)


print(sum)
