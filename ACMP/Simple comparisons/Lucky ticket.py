inp = list(input())
if len(inp)%2!=0:
    inp = [0] + inp
half = len(inp)//2
left_arr = inp[:half]
right_arr = inp[half:]
del half
left = 0
right = 0
while len(left_arr) != 0:
    left += int(left_arr[0])
    left_arr = left_arr[1:]
    right += int(right_arr[0])
    right_arr = right_arr[1:]
if right == left:
    print("YES")
else:
    print("NO")
