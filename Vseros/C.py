inp = input().split(" ")
n, k = int(inp[0]), int(inp[1])
inp = input().split(" ")
if (int(inp[0]) == n and int(inp[1]) == n):
      answ = "-1"
else:
      if int(inp[1]) == n:
            inp[0] = int(inp[0]) + 1
            inp[1] = 0
      elif int(inp[1]) < n:
            inp[1] = int(inp[1]) + 1
      answ = str(inp[0]) + " " + str(inp[1])
print(answ)
