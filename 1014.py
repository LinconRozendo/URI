#include<stdio.h>
import math

x = input().split()
y = input().split()

x1, y1 = float(x[0]), float(x[1])
x2, y2 = float(y[0]), float(y[1])

print('%.4f' %(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))))


