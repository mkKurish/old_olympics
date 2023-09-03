inp = input().split(' ')
X = int(inp[0]) * 100
P = int(inp[1])
Y = int(inp[2]) * 100
year = 0
while X < Y:
    X = X * (1 + P/100)
    X = X // 1
    year += 1
print(year)
