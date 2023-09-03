N = int(input())
arr = []
counter = 0
while N != 0:
      arr.append(int(input()))
      N -= 1
while len(arr) > 2:
      min_ind = 1
      i = 1
      while i < len(arr) - 1:
            if i != len(arr) - 2:
                  if arr[min_ind] * (arr[min_ind - 1] + arr[min_ind + 1]) > arr[i] * (arr[i - 1] + arr[i + 1]):
                        min_ind = i
            else:
                  if arr[min_ind] * (arr[min_ind - 1] + arr[min_ind + 1]) < arr[i] * (arr[i - 1] + arr[i + 1]):
                        min_ind = i
            i += 1
      counter += arr[min_ind] * (arr[min_ind - 1] + arr[min_ind + 1])
      print(arr[min_ind])
      del arr[min_ind]
print(counter)
