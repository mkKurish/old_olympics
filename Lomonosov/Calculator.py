import math
def dectofif(num):
      s = ["0", "1", "2", "B", "A"]
      ost = num % 1
      j = 0
      res = []
      while j < 11:
            ost *= 5
            cel = ost // 1
            ost = ost % 1
            res.append(s[int(cel)])
            j += 1
      num = math.floor(num)
      k = 0
      lst = []
      rlst = []
      neg = False
      if num < 0:
            num = -num
            neg = True
      if num == 0:
            k += 1
            lst.append("0")
      else:
            while num != 0:
                  rem = int(num % 5)
                  num = num // 5
                  if rem > 5 // 2:
                        num += 1
                  if neg and rem > 0:
                        rem = 5 - rem
                  k += 1
                  lst.append(s[int(rem)])
      i = 0
      while i < k:
            rlst.append(lst[k-1-i])
            i += 1
      while len(rlst) < 16:
            rlst = ["0"] + rlst
      lst = rlst + res
      i = 0
      answer = ""
      while i < len(lst):
            answer += lst[i]
            i += 1
      print(answer)
      return
inp = input().split(" ")
i = 0
stack = []
myBool = True
while i < len(inp):
      if inp[i] == "+":
            stack[len(stack)-2] = stack[len(stack)-2] + stack[len(stack)-1]
            del stack[len(stack)-1]
      elif inp[i] == "-":
            stack[len(stack)-2] = stack[len(stack)-2] - stack[len(stack)-1]
            del stack[len(stack)-1]
      elif inp[i] == "*":
            stack[len(stack)-2] = stack[len(stack)-2] * stack[len(stack)-1]
            del stack[len(stack)-1]           
      elif inp[i] == "/":
            if stack[len(stack)-1] != 0:
                  stack[len(stack)-2] = stack[len(stack)-2] / stack[len(stack)-1]
                  del stack[len(stack)-1]
            else:
                  print("ERROR")
                  myBool = False
      else:
            stack.append(float(inp[i]))
      i += 1
if myBool:
      dectofif(stack[0])
