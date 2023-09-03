X = 500000000
now = 500000000
print(X)
sign = input()
while sign != "=":
    if now > 1:
        now //= 2
    if sign == ">":
        X += now
    else:
        X -= now
    print(X)
    sign = input()
    

    
