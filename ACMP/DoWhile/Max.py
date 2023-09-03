def my_sort (arr):
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1 - i:
            if int(arr[j]) > int(arr[j + 1]):
                bubble = int(arr[j + 1])
                arr[j + 1] = int(arr[j])
                arr[j] = bubble
            j += 1
        i += 1
    return arr

array = input().split(' ')
ind = array.index('0')
array = my_sort(array[:ind])
i = len(array) - 1
m = int(array[i])
k = 0
while int(array[i]) == m:
    i -= 1
    k += 1
    if  i<0:
        break
print(k)
