num = int(input())
x = 1
answ = ""
if num > 0:
    while x**2 <= num:
        answ += str(x**2) + " "
        x += 1
else:
    answ = "0"
print(answ)
