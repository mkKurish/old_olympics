inp = input().split()
arr=[]
while len(inp) != 0:
      arr.append(int(inp[0]))
      del inp[0]
i = 0
while i < len(arr):
      j = 0
      while j < len(arr) - 1 - i:
            if arr[j] > arr[j + 1]:
                  tmp = arr[j]
                  arr[j] = arr[j + 1]
                  arr[j + 1] = tmp
            j += 1
      i += 1
print((arr[0] * arr[1]) + (arr[2] * arr[3]))
