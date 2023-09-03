def comparison (B1, B2):
    if B1[0] >= B2[0] and B1[1] >= B2[1] and B1[2] >= B2[2]:
        return True
    return False
inp = input().split(' ')
box1 = [ int(inp[0]),
         int(inp[1]),
         int(inp[2])]
inp = input().split(' ')
box2 = [ int(inp[0]),
         int(inp[1]),
         int(inp[2])]
del inp
answ = "Boxes are incomparable"
box1 = sorted(box1)
box2 = sorted(box2)
if box1 == box2:
    answ = "Boxes are equal"
elif comparison(box1, box2):
    answ = "The first box is larger than the second one"
elif comparison(box2, box1):
    answ = "The first box is smaller than the second one"
print(answ)
