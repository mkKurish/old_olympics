inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])
def NOD (a ,b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b
def NOK (n , m):
    return (n * m)//NOD(n , m)
out = NOK(n , m) // m
print(out)
    
