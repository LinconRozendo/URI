#include<stdio.h>
import math

x = input().split()

a, b, c = float(x[0]), float(x[1]), float(x[2])

if a != 0:
    if b != 0 and ((b ** 2) - 4 * a * c) >= 0:
        r1 = ((- b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a))
        r2 = ((- b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a))

        print('R1 = %.5f' %(r1))
        print('R2 = %.5f' %(r2))
    else:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')



