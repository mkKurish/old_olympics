def truth(string, colmn):
      """
      функция проверяет четырёхсвязность изображения
      """
      strok = len(string) / colmn
      z = 0
      inds = []
      while z != strok - 1:
            substring1 = string[z*colmn : colmn*(z+1)]
            substring2 = string[colmn*(z+1):colmn*(z+2)]
            k = 0
            while k < colmn:
                  if (substring1[k] == substring2[k] == "#"):
                              inds.append(z*colmn+k)
                              inds.append(colmn*(z+1)+k)
                  if k < colmn -1:
                        if(substring1[k] == substring1[k+1] == "#"):
                              inds.append(z*colmn+k)
                              inds.append(z*colmn+k+1)
                        if(substring2[k] == substring2[k+1] == "#"):
                              inds.append(colmn*(z+1)+k)
                              inds.append(colmn*(z+1)+k+1)
                  k += 1
            z += 1
      itr = 0
      allind = []
      while itr != len(string):
            if string[itr] == "#":
                  allind.append(itr)
            itr += 1
      return set(allind) == set(inds)
#Принимаем значение:
string = input()
#Перебираем делители:
i = 1
while i != len(string):
      if len(string) % i == 0:
            #Если изображение четырёхсвязное, то отрисовываем:
            if truth(string, i):
                  j = len(string) / i
                  while j != 0:
                        string2 = string[:i]
                        string = string[i:]
                        print(string2)
                        j -= 1
                  break
      i += 1
