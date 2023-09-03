inp = input().split(' ')
i, j = int(inp[0]), int(inp[1])
M = {0: 0, 1: 1}
def fib(n):
    b, c = 0, 1
    if n == 1:
        return 1
    for i in range(0, n):
        tmp = b
        b = ( b + c ) % (10**9)
        c = tmp
    return b
while i * j != 0:
    if i > j:
        i %= j
    else:
        j %= i
print(fib(j+i))
