num = int(input())
watermelons = input().split(' ')
max = 0
min = 30000
for x in watermelons:
    if int(x) > max:
        max = int(x)
    if int(x) < min:
        min = int(x)
print(min, max)
