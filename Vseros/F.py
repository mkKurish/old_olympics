n = int(input())
i = 1
mcounter = -1
num = -1
while i <= n:
      counter = 0
      j = i
      while j != 0:
            if i % j == 0:
                  counter += 1
            j -= 1
      if counter > mcounter or mcounter == -1:
            mcounter = counter
            num = i
      i += 1
print(num)
print(mcounter)
      
