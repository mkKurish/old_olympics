def recoordinator (a:str):
    number = ord(a[0]) - 64
    new_coord = []
    new_coord.append(number); new_coord.append(int(a[1]))
    return new_coord

def Pawn (coordX, coordY, seccoordX, seccoordY):
    global answ
    answ = ""
    if coordX == seccoordX:
        if coordY == 2:
            if seccoordY == 4 or seccoordY == 3:
                answ = answ + "\nPawn"
                print("Pawn")
        elif seccoordY == coordY + 1 and coordY != 1 and coordY != 8:
            answ = answ + "\nPawn"
            print("Pawn")
    return

def Rook (coordX, coordY, seccoordX, seccoordY):
    global answ
    if coordX == seccoordX or coordY == seccoordY:
        answ = answ + "\nRook"
        print("Rook")
    return

def Bishop (coordX, coordY, seccoordX, seccoordY):
    global answ
    diff = coordX - seccoordX
    if coordY + diff == seccoordY or coordY - diff == seccoordY:
        answ = answ + "\nBishop"
        print("Bishop")
    return

def Knight (coordX, coordY, seccoordX, seccoordY):
    global answ
    Sx = coordX - seccoordX
    Sy = coordY - seccoordY
    if Sx < 0:
        Sx = - Sx
    if Sy < 0:
        Sy = - Sy
    if (Sx == 2 and Sy == 1) or (Sx == 1 and Sy == 2):
        answ = answ + "\nKnight"
        print("Knight")
    return

def Queen (coordX, coordY, seccoordX, seccoordY):
    global answ
    if coordX != seccoordX:
        diff = coordX - seccoordX
        if coordY + diff == seccoordY or coordY - diff == seccoordY or coordY == seccoordY:
            answ = answ + "\nQueen"
            print("Queen")
    else:
        answ = answ + "\nQueen"
        print("Queen")
    return

def King (coordX, coordY, seccoordX, seccoordY):
    global answ
    diffX = coordX - seccoordX
    diffY = coordY - seccoordY
    if diffX < 0:
        diffX = - diffX
    if diffY < 0:
        diffY = - diffY
    if diffX < 2 and diffY < 2:
        answ = answ + "\nKing"
        print("King")
    return

inp = input().split(" ")
cell1 = recoordinator(str(inp[0]))
cell2 = recoordinator(str(inp[1]))
del inp

Pawn(int(cell1[0]), int(cell1[1]), int(cell2[0]), int(cell2[1]))
Rook(int(cell1[0]), int(cell1[1]), int(cell2[0]), int(cell2[1]))
Bishop(int(cell1[0]), int(cell1[1]), int(cell2[0]), int(cell2[1]))
Knight(int(cell1[0]), int(cell1[1]), int(cell2[0]), int(cell2[1]))
Queen(int(cell1[0]), int(cell1[1]), int(cell2[0]), int(cell2[1]))
King(int(cell1[0]), int(cell1[1]), int(cell2[0]), int(cell2[1]))
if answ == "":
    answ = "Nobody"
    print("Nobody")
#print(f"{answ}")
