pics = int(input())
res = 1
if pics %2 ==0:
      while pics > 1:
            res *= (pics-1)*2
            pics -= 2
      print(res%1000000007)
else:
      print(0)
