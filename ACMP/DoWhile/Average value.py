arr = input().split(' ')
answer = 0
key = 0
for item in arr:
    if int(item) == 0:
        break
    answer += int(item)
    key += 1
print(answer/key)
