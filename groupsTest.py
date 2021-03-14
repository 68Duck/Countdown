
combination = ['+75', '*50', '+8', '*5', '+4', '*3']

solution = ""
if combination[0][0:1] == "+":
    combination[0] = combination[0][1:len(combination[0])]#
previousSign = None
startBrackets = 0
for i in range(len(combination)):
    if i != len(combination)-1:
        nextSign = combination[i+1][0:1]
    sign = combination[i][0:1]
    numberPart = combination[i][1:len(combination[i])]
    if sign == "*":
        sign = "x"
    elif sign == "/":
        sign = "÷"
    if i != 0: #can only be the first as doesn't have the sign
        # if i == 1:
        if sign == "+" or sign == "-":
            if nextSign == "+" or nextSign == "-":
                number = sign + " " + numberPart + " "
            else:
                number = sign + " " + numberPart + ") "
                startBrackets += 1
        else:
            number = sign + " " + numberPart + " "

    else:
        if sign == "+":
            number = numberPart + " "
        else:
            number = sign + numberPart + " "
    previousSign = sign[:]
    solution = solution + number

for j in range(startBrackets):
    solution = "(" + solution

print(solution)
