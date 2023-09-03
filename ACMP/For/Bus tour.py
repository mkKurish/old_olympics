quantity = int(input())
sizes = input().split(' ')
crash = False
for k in sizes:
    if int(k) <= 437:
        print("Crash " + str(sizes.index(k) + 1))
        crash = True
        break
if crash == False:
    print("No crash")
