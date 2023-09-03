inp = input().split(' ')
X = float(inp[0])
Y = float(inp[1])
lnY = lnX = 0
if X % 1!= 0:
    lnX = len(str(X % 1)) - 2
if Y % 1!= 0:
    lnY = len(str(Y % 1)) - 2
ln = 0
if lnY > lnX:
    ln = lnY
else:
    ln = lnX
while ln != 0:
    X *= 10
    Y *= 10
    ln -= 1
Y = int(Y)
X = int(X)
day = 1
while X < Y:
    X = X * 115
    Y = Y * 100
    day += 1
print(day)
