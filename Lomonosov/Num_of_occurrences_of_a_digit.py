D = int(input())
L = int(input())
N = input()
numHex = []
i = 0
while i < len(N):
      if N[i] == "A" :
            numHex.append(10)
      elif N[i] == "B" :
            numHex.append(11)
      elif N[i] == "C" :
            numHex.append(12)
      elif N[i] == "D" :
            numHex.append(13)
      elif N[i] == "E" :
            numHex.append(14)
      elif N[i] == "F" :
            numHex.append(15)
      else:
            numHex.append(N[i])
      i += 1
numDub = ""
i = 0
while i < len(numHex):
      k = 0
      binar = ""
      while (k != 4):
            mod = int(numHex[i]) % 2
            binar = str(mod) + binar
            k += 1
            numHex[i] = int(numHex[i]) // 2
      numDub += binar
      i += 1
i = 0
numDec = 0
while i < len(numDub):
      numDec += int(numDub[i])*2**(len(numDub)-1-i)
      i += 1
numOct = ""
i = 0
myBool = True
while (myBool):
      mod = numDec % 8
      numOct = str(mod) + numOct
      numDec = numDec // 8
      if numDec == 0:
            myBool = False
i = 0
counter = 0
while i < len(numOct):
      if int(numOct[i]) == D:
            counter += 1
      i += 1
print(int(counter))
