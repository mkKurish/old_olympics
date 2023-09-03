inp = input().split(' ')
A = int(inp[0])
B = int(inp[1])
while A * B != 0:
    if A > B:
        A %= B
    else:
        B %= A
print(A + B)
