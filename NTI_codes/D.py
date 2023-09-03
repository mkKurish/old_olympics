string = "..#.#.#.###.#.##"
i = 4
j = 4
j = len(string) / i
while j != 0:
      string2 = string[:i]
      string = string[i:]
      print(string2)
      j -= 1

print()
string = "..#.#.#.###.#.##"


strok = len(string) / i
z = 0
res = True
inds = []
while z != strok - 1:
      substring1 = string[z*i : i*(z+1)]
      substring2 = string[i*(z+1):i*(z+2)]
      print(substring1, substring2)
      k = 0
      while k != i-1:
            if (substring1[k] == substring2[k] == "#"):
                  inds.append(z*i+k)
                  inds.append(i*(z+1)+k)
            if(substring1[k] == substring1[k+1] == "#"):
                  inds.append(z*i+k)
                  inds.append(z*i+k+1)
            if(substring2[k] == substring2[k+1] == "#"):
                  inds.append(i*(z+1)+k)
                  inds.append(i*(z+1)+k+1)
            k += 1
      z += 1
itr = 0
allind = []
while itr != len(string):
      if string[itr] == "#":
            allind.append(itr)
      itr += 1

print(set(allind) == set(inds))
