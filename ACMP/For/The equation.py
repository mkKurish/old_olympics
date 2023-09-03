inp = input().split(' ')
answ = ""
for x in range(-100, 101):
    if (x**3)*int(inp[0])+(x**2)*int(inp[1])+x*int(inp[2])+int(inp[3]) == 0:
        answ += str(x) + " "
print(answ)
