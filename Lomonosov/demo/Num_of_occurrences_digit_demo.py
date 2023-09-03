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
print(numHex)
numDub = ""
i = 0
while i < len(numHex):
      k = 0
      binar = "00000"
      while (k != 4):
            mod = int(numHex[i]) % 2
            print("mod " + str(mod))
            #numHex[i] = int(numHex[i]) // 2
            if numHex[i] != 0:
                  if len(binar) == 5:
                        binar = str(mod)
                  else:
                        binar = str(10*int(binar)) + str(mod)
            else:
                  binar = "0" + binar
            k += 1
            print("binar " + binar)
            print("numHex[i] " + str(numHex[i]))
            numHex[i] = int(numHex[i]) // 2
            print("numHex[i] " + str(numHex[i]))
      numDub += binar
      i += 1
print(numDub)
