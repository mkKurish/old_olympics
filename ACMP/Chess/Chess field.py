inp = input().split(' ')
cell1 = []
cell2 = []
cell1.append(inp[0]); cell1.append(inp[1])
cell2.append(inp[2]); cell2.append(inp[3])
del inp
# Если обе координаты четные или нечетные - клетка черная.
if int(cell1[0]) % 2 == 0:
    if int(cell1[1]) % 2 == 0:
        CELL1 = True # True - черная клетка.
    else:
        CELL1 = False # False - белая клетка.
else:
    if int(cell1[1]) % 2 == 0:
        CELL1 = False
    else:
        CELL1 = True

if int(cell2[0]) % 2 == 0:
    if int(cell2[1]) % 2 == 0:
        CELL2 = True # True - черная клетка.
    else:
        CELL2 = False # False - белая клетка.
else:
    if int(cell2[1]) % 2 == 0:
        CELL2 = False
    else:
        CELL2 = True
if CELL1 == CELL2:
    print("YES")
else:
    print("NO")
