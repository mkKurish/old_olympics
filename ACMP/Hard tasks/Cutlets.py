inp = input().split(' ')
skovoroda = int(inp[0])
minut = int(inp[1])
kotlet = int(inp[2])
answ = 0
if kotlet == 0:
    print(answ)
else:
    if skovoroda != 0:
        if kotlet <= skovoroda:
            answ = minut * 2
        else:
            answ = 2 * kotlet // skovoroda * minut;
            if (2 * kotlet % skovoroda !=0):
                answ += minut;
        print(answ)
    else:
        print(answ)
