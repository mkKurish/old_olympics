def period (sequence, P):
      T = 1
      res = len(sequence)
      while T <= P:
            sequence2 = sequence
            part = sequence[:T]
            while True:
                  if (part == sequence2[:T]):
                        sequence2 = sequence2[T:]
                  else:
                        z = 0
                        while z != len(part):
                              if part[:z] != sequence2[:z]:
                                    sequence2 = sequence2[z-1:]
                                    break;
                              z += 1
                        if res > len(sequence2):
                              res = len(sequence2)
                        break;
            T += 1
      return(res)
P = int(input())
sequence = input()
print(period(sequence, P))

