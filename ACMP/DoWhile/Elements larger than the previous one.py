arr = input().split(' ')
answ = 0
ind = arr.index('0')
arr = arr[:ind]
item = 0
while item + 1 <= len(arr) -1:
    if int(arr[item + 1]) > int(arr[item]):
        answ += 1
    item += 1
print(answ)
