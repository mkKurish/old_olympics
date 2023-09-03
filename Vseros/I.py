def maximum(arr, res):
      max = arr[0][1]
      i = 0
      j = 0
      boolean = True
      while i < len(arr):
            while j < len(res):
                  if i == res[j]:
                        boolean = False
                  j += 1
            if arr[i][1] > max and boolean:
                  max = arr[i][1]
            i += 1
            boolean = True
      return max
def minimum(arr, arg):
      i = 0
      min = arr[0][0]
      while i < len(arr):
            if arr[i][0] < min and arr[i][1] == arg:
                  min = arr[i][0]
            i += 1
      return min
N = int(input())
i = 0
array = []
while i < N:
      inp = input().split(" ")
      array.append([])
      array[i].append(int(inp[0]))
      array[i].append(int(inp[1]))
      i += 1
i = 0
destr = 0
res = []
while i < len(array):
      if array[i][1] == maximum(array, res) and array[i][0] == minimum(array, maximum(array, res)):
            res.append(i)
      i += 1
print(res)
