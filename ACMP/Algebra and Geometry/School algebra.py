inp = input().split(' ')

a, b, c = int(inp[0]), int(inp[1]), int(inp[2])
answ = ""
if a != 0:
    answ += str(a)

if b != 0:
    if a == 0:
        if b == 1:
            answ += "x"
        elif b == -1:
            answ += "-x"
        else:
            answ += str(b) + "x"
    else:
        if b == 1:
            answ += "+x"
        elif b == -1:
            answ += "-x"
        elif b > 0:
            answ += "+" + str(b) + "x"
        else:
            answ += str(b) + "x"

if c != 0:
    if a == 0 and b == 0:
        if c == 1:
            answ += "y"
        elif c == -1:
            answ += "-y"
        else:
            answ += str(c) + "y"
    else:
        if c == 1:
            answ += "+y"
        elif c == -1:
            answ += "-y"
        elif c > 0:
            answ += "+" + str(c) + "y"
        else:
            answ += str(c) + "y"
if answ == "":
    answ = "0"
print(answ)
