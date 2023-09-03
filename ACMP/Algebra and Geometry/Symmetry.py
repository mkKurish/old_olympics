def symetry (p, crd):
    distance = abs(crd - p)
    if p < crd:
        return (crd + distance)
    else:
        return (crd - distance)
    
line = input().split(' ')
coord_1, coord_2 = [int(line[0]),int(line[1])],[int(line[2]),int(line[3])]
del line
point1 = input().split(' ')
point1 = [int(point1[0]), int(point1[1])]
point2 =[]
if coord_1[0] != coord_2[0]:
    point2.append(point1[0])
    point2.append(symetry(point1[1],coord_1[1]))
else:
    point2.append(symetry(point1[0],coord_1[0]))
    point2.append(point1[1])
print(point2[0], point2[1])
