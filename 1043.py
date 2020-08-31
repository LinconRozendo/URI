#include<stdio.h>

n = input().split()

a, b, c =  float(n[0]), float(n[1]), float(n[2])

if (b - c) < a and a < (b + c):
    if (a - c) < b and  b < (a + c):
        if (a - b) < c and c < (a + b):
            print('Perimetro = %.1f' %(a + b + c))
        else:
            print('Area = %.1f' %(((a + b) * c)/2))
    else:
        print('Area = %.1f' %(((a + b) * c)/2))
else:
    print('Area = %.1f' %(((a + b) * c)/2))

