num = int(input())
negative = False
result = ""
if num < 0:
      negative = True
      num = -num
array = ["0", "1", "$"]
while num > 0:
      mod = int(num % 3)
      tmp = num // 3
      result = array[mod] + result
      if mod <= 1:
            num = tmp
      else:
            num = tmp + 1
if negative:
      i = 0
      n_res = result
      result = ""
      while len(n_res) > i:
            if n_res[i] == "$":
                  result += "1"
            elif n_res[i] == "1":
                  result += "$"
            else:
                  result += "0"
            i += 1
print(result)
