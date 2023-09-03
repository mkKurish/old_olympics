def maxW(lst, used):
      i = 0
      max = 0
      while i < len(lst):
            if lst[i][1] > max and notInArr(lst[i][1], used):
                  max = lst[i][1]
            i += 1
      return max
def notInArr(num, arr):
      i = 0
      while i < len(arr):
            if num == arr[i]:
                  return False
            i += 1
      return True
def minD(lst):
      i = 0
      min = lst[0]
      while i < len(lst):
            if lst[i] < min:
                  min = lst[i]
            i += 1
      return min
N = int(input())
i = 0
ar = []
while i < N:
      ar.append([])
      inp = input().split(' ')
      ar[i].append(int(inp[0]))
      ar[i].append(int(inp[1]))
      i += 1
i = 0
res = []
lstw = []
late = []
while i < N:
      indsw = []
      while len(indsw) == 0:
            maxw = maxW(ar, lstw)
            k = 0
            while k < N:
                  if ar[k][1] == maxw and notInArr(k, res):
                        indsw.append(k)
                  k += 1
            if len(indsw) == 0:
                  lstw.append(maxw)
      mind = minD(indsw)
      print("indsw")
      print(indsw)
      k = 0
      while k < len(indsw):
            print("mind " + str(mind))
            print("notInArr(indsw[k], res) " + str(notInArr(indsw[k], res)))
            print("notInArr(indsw[k], late) " + str(notInArr(indsw[k], late)))
            print("late " + str(late))
            if indsw[k] == mind and notInArr(indsw[k], res) and notInArr(indsw[k], late):
                  res.append(indsw[k])
                  print("indsw[k] = ", end = "")
                  print(indsw[k])
            k += 1
      i += 1
      q = 0
      print("i = ", end= "")
      print(i)
      while q < len(ar):
            if ar[q][0] <= i and notInArr(q, late) and notInArr(q, res):
                  print("block")
                  print(i)
                  print(ar[q][0])
                  late.append(q)
            q += 1
res = res + late
print(res)

"""
5
1 1
1 2
1 3
2 3
3 1
"""
