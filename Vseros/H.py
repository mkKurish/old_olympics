def time():
      global personsL
      global personsR
      personsL[max_player(personsL)][2] = False
      personsL[min_player(personsL)][2] = True
      personsR[max_player(personsR)][2] = False
      personsR[min_player(personsR)][2] = True
      i = 0
      while i < len(personsL):
            if personsL[i][2] == True:
                 personsL[i][1] += 1
            i += 1
      i = 0
      while i < len(personsR):
            if personsR[i][2] == True:
                 personsR[i][1] += 1
            i += 1
      return
def min_player(array):
      k = 0
      min = array[0][1]
      ind = 0
      while k < len(array):
            if array[k][2] == False:
                  if array[k][1] <= min:
                        min = array[k][1]
                        ind = k
            k += 1
      return ind
def max_player(array):
      k = 0
      max = array[0][1]
      ind = 0
      while k < len(array):
            if array[k][2] == True:
                  if array[k][1] > max:
                        max = array[k][1]
                        ind = k
            k += 1
      return ind
startData = input().split()
startData[0], startData[1], startData[2] = int(startData[0]), int(startData[1]), int(startData[2])
#array = [players, replacement, activePlayers]
i = 0
personsL = []
personsR = []
lc = 0
rc = 0
#array = [person:[name, counter, nowStat], ...]
while i < startData[0]:
      if i % 2 == 0:
            personsL.append([])
            personsL[lc].append(input())
            personsL[lc].append(0)
            personsL[lc].append(False)
            lc += 1
      else:
            personsR.append([])
            personsR[rc].append(input())
            personsR[rc].append(0)
            personsR[rc].append(False)
            rc += 1
      i += 1
del rc , lc
i = 0
while i < startData[2]:
      personsL[i][2] = True
      personsR[i][2] = True
      i += 1
i = 0
while i < startData[1]:
      time()
      i += 1
i = 0
answ = []
while i < startData[1]:
      if personsL[i][2] == True:
            answ.append(personsL[i][0])
      if personsR[i][2] == True:
            answ.append(personsR[i][0])
      i += 1
print(sorted(answ))
