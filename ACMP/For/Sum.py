num = int(input())
if num > 0:
    if num %2 != 0:
        answ = (num // 2 + 1) * num
    else:
        answ = (num // 2) * (num + 1)
    print(answ)
else:
    num = - num
    if num %2 != 0:
        answ = (num // 2 + 1) * num - 1
    else:
        answ = (num // 2) * (num + 1) - 1
    print(-answ)
