peoples = int(input())
i = 1
reference = 0
ind = -1
while i <= peoples:
    inp = input().split(' ')
    if int(inp[1]) == 0:
        i += 1
        continue
    if int(inp[0]) > reference:
        ind = i
        reference = int(inp[0])
    i += 1
print(ind)
