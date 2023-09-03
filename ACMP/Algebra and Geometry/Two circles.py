inp = input().split(' ')
X1 = int(inp[0])
Y1 = int(inp[1])
R1 = int(inp[2])
inp = input().split(' ')
X2 = int(inp[0])
Y2 = int(inp[1])
R2 = int(inp[2])

X = X2 - X1
Y = Y2 - Y1
distance = (X**2+Y**2)**0.5
if distance + R1 <= R2 or distance + R2 <= R1:
    print("NO")
elif distance < (R1 + R2)**2:
    print("YES")
else:
    print("NO")
