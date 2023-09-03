num = int(input())
x = 1
answ = 1
while x <= num:
    if num % x == 0:
        if x != 1:
            answ = x
            break
    x += 1
print(answ)
            
