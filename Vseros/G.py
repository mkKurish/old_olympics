def func(n, s):
      if s == 1:
            global counter
            counter += 1
            return
      q = n//s
      while q >= 0:
            func(((n%s)+q*s), s-2)
            q -= 1
      return
n = int(input())
if n%2 == 0:
      s = n -1
else:
      s = n
counter = 0
func(n, s)
print(counter)
