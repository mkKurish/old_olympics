def toOctArr(num):
      octo = ""
      while num != 0:
            octo = str(num % 8) + octo
            num = num // 8
      octo = list(octo)
      return octo
def toOctNum(num):
      octo = ""
      while num != 0:
            octo = str(num % 8) + octo
            num = num // 8
      return int(octo)
def octSum(res, num):
      if res%10 + num > 7:
            res += 10 + num - 8
      else:
            res += num
      return res
def sumOfDigit(arr):
      i = 0
      counter = 0
      while i < len(arr):
            counter = octSum(counter, int(arr[i]))
            i += 1
      return counter
def toDecNum(num):
      i = 0
      counter = 0
      num = list(str(num))
      while i < len(num):
            counter += int(num[len(num) - i - 1]) * 8 ** i
            i += 1
      return counter
def notIncludeZero(arr):
      i = 0
      mybool = True
      while i < len(arr):
            if int(arr[i]) == 0:
                  mybool = False
            i += 1
      return mybool
k = 0
answer = 0
while True:
      k = k + 1
      c = toOctArr(k)
      if c[len(c) - 1] == c[len(c) - 2] and toDecNum(sumOfDigit(toOctArr(k))) == 7 and notIncludeZero(toOctArr(k)):
            answer += 1
            print(toOctNum(k))
            print("answer =    " + str(answer))


            
