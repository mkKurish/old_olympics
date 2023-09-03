ocherednoe_skychnoe_nazvanie = input().split(' ')
N,x,y = int(ocherednoe_skychnoe_nazvanie[0]),int(ocherednoe_skychnoe_nazvanie[1]),int(ocherednoe_skychnoe_nazvanie[2])
del ocherednoe_skychnoe_nazvanie #you have completed your mission, press f...
if x > y:
    x,y=y,x
import math
t = math.ceil(((N - 1) * x * y) / (x + y))
print(t + x)
