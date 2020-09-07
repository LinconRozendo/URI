#include<stdio.h>

v = []

for i in range(0, 100):
    v.append(float(input()))

for f in range(0, 100):
    if v[f] <= 10:
        print('A[%d] = %.1f' %(f, v[f]))