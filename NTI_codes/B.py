import math
def area (Xobj, Yobj, X1, Y1, X2, Y2):
      """
      Рассчитываем площадь для треугольника
      - объект, точка, точка -
      """
      a = ((X1 - X2)**2+(Y1 - Y2)**2)**0.5
      b = ((Xobj - X2)**2+(Yobj - Y2)**2)**0.5
      c = ((X1 - Xobj)**2+(Y1 - Yobj)**2)**0.5
      p = (a + b + c) / 2.0
      ar = (p * (p - a) * (p - b) * (p - c))**0.5
      return ar
#Принимаем координаты отрезка AB:
string = input().split(" ")
Xa, Ya, Xb, Yb = int(string[0]), int(string[1]), int(string[2]), int(string[3])
NnM = input().split(" ")
N = int(NnM[0])
M = int(NnM[1])
#Создаем списки для координат звезд и планет:
arrNx = []
arrNy = []
arrMx = []
arrMy = []
#Заполняем списки координат звезд и планет:
i = 0
while i != N:
      string = input().split(" ")
      arrNx.append(int(string[0]))
      arrNy.append(int(string[1]))
      i += 1
i = 0
while i != M:
      string = input().split(" ")
      arrMx.append(int(string[0]))
      arrMy.append(int(string[1]))
      i += 1
#Определяем прямую, на которой лежит AB:
k = (Ya - Yb)/(Xa - Xb)
b = Yb - k * Xb
#Определяем какие из планет и звезд лежат под прямой, какие лежат на прямой, а какие - над:
overN = []
underN = []
onN = []
overM = []
underM = []
onM = []
i = 0
while i < len(arrNx):
      if (arrNy[i]>k*arrNx[i]+b):
            overN.append([arrNx[i], arrNy[i]])
      elif (arrNy[i]<k*arrNx[i]+b):
            underN.append([arrNx[i], arrNy[i]])
      else:
            onN.append([arrNx[i], arrNy[i]])
      i += 1
i = 0
while i < len(arrMx):
      if (arrMy[i]>k*arrMx[i]+b):
            overM.append([arrMx[i], arrMy[i]])
      elif (arrMy[i]<k*arrMx[i]+b):
            underM.append([arrMx[i], arrMy[i]])
      else:
            onM.append([arrMx[i], arrMy[i]])
      i += 1
#Для каждого объекта рассчитаем эффект и записываем в список:
singleEffect = []
i = 0
while i != len(overN):
      singleEffect.append(area(overN[i][0], overN[i][1], Xa, Ya, Xb, Yb))
      i += 1
i = 0
while i != len(underN):
      singleEffect.append(area(underN[i][0], underN[i][1], Xa, Ya, Xb, Yb))
      i += 1
i = 0
while i != len(onN):
      singleEffect.append(area(onN[i][0], onN[i][1], Xa, Ya, Xb, Yb))
      i += 1
i = 0
while i != len(overM):
      singleEffect.append(area(overM[i][0], overM[i][1], Xa, Ya, Xb, Yb))
      i += 1
i = 0
while i != len(underM):
      singleEffect.append(area(underM[i][0], underM[i][1], Xa, Ya, Xb, Yb))
      i += 1
i = 0
while i != len(onM):
      singleEffect.append(area(onM[i][0], onM[i][1], Xa, Ya, Xb, Yb))
      i += 1
#Рассчитываем и записываем эффект для всех пар "звезда - планета":
doubleEffect = []
i = 0
while i != len(overN):
      j = 0
      eff1 = area(overN[i][0], overN[i][1], Xa, Ya, Xb, Yb)
      while j != len(underM):
            eff2 = area(underM[j][0], underM[j][1], Xa, Ya, Xb, Yb)
            doubleEffect.append(eff1 * eff2)
            j += 1
      i += 1
i = 0
while i != len(underN):
      j = 0
      eff1 = area(underN[i][0], underN[i][1], Xa, Ya, Xb, Yb)
      while j != len(overM):
            eff2 = area(overM[j][0], overM[j][1], Xa, Ya, Xb, Yb)
            doubleEffect.append(eff1 * eff2)
            j += 1
      i += 1
#Складываем два списка эффектов:
effects = singleEffect + doubleEffect
#Выводим наибольший элемент:
print('{:.2f}'.format(round(max(effects), 2)))
