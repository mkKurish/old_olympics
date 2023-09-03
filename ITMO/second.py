N = 750
counter = 0
while N <1002:
      k = N
      while k > 10:
            k = (k//10)*3 + k%10
      if k == 7:
            print("Yes")
            counter += 1
      N += 1
print(counter)
      
