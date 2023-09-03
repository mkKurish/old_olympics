num = int(input())
vol_0 = 0
vol_1 = 0
while num != 0:
    t = int(input())
    if t == 1:
        vol_1 += 1
    else:
        vol_0 += 1
    num -= 1
if vol_0 >= vol_1:
    print(vol_1)
else:
    print(vol_0)
    
