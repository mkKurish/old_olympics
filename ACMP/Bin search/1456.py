def sort(arr):
    leng = len(str(max(arr)))
    rang = 10
    i=0
    while i < len(arr):
        ARR = [[] for x in range(rang)]
        for k in arr:
            fig = (int(k)//(10**i)) % 10
            ARR[fig].append(k)
        arr = []
        for x in range(rang):
            arr = arr + ARR[x]
        i+=1
    return arr
def podezdov (komnat, etaji, kr, nekr, kratnost):
    ostk = 1
    vsego = (etaji//kratnost)*kr+(etaji-(etaji//kratnost))*nekr
    ostk = vsego - komnat % vsego
    komnat += ostk
    result = komnat // vsego
    res = result*vsego// result
    return res
def na_kakom_etaje(o_p, num, et, kr, x, y):
    in_pod = num % o_p
    if in_pod == 0:
        in_pod = o_p
    answ = (in_pod*kr)//(x+y*kr-y)
    last = (answ//kr)*x+(answ-(answ//kr))*y
    if answ % kr == 0:
        if (in_pod <= last and in_pod > last-x) == False:
            answ += 1
    else:
        if (in_pod <= last and in_pod > last-y) == False:
            answ += 1
    return answ
inp = input().split(" ")
n, k, x, y = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
q = int(input())
nums = list(input().split(" "))
nums2 = sort(nums)
p = podezdov(int(nums2[q-1]), n, x, y, k)
AAA = 0
while AAA < len(nums): 
    print(na_kakom_etaje(p, int(nums[AAA]), n, k, x, y))
    AAA += 1
