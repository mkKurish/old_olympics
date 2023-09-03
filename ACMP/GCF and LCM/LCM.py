inp = input().split(' ')
A = int(inp[0])
B = int(inp[1])
def simple(X):
    res = [1]
    i = 2
    while i <= X:
        while X % i == 0:
            res.append(i)
            X //= i
        i += 1
    return res
la = max(simple(A))
A = simple(A)
lb = max(simple(B))
B = simple(B)
i = 1
answ = 1
while i <= la and i <= lb:
    while i in A and i in B:
        answ *= i
        A.remove(i)
        B.remove(i)
    i += 1
if len(A) != 0:
    x = 0
    while x < len(A):
        answ *= A[x]
        x += 1
if len(B) != 0:
    x = 0
    while x < len(B):
        answ *= B[x]
        x += 1
print(answ)
