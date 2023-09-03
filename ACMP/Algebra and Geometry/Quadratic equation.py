inp = input().split(' ')
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])
val = 0
D = b**2 - 4*a*c
if a != 0:
    if D < 0:
        val = 0
        print(0)
    if D == 0:
        val = 1
        x = -b/(2*a)
        print(f"{val}\n{x}")
    if D > 0:
        val = 2
        x1 = ((-b + D**0.5)/(2*a))
        x2 = ((-b - D**0.5)/(2*a))
        print(f"{val}\n{x1}\n{x2}")
else:
    if b != 0:
        val = 1
        x = -c/b
        print(f"{val}\n{x}")
    else:
        if c != 0:
            val = 0
            print(f"{val}")
        else:
            val = -1
            print(f"{val}")
