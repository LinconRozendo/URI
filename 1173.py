#include<stdio.h>

v = []

n = int(input())

for i in range(0, 10):
    if i == 0:
        v.append(n)
    else:
        n *= 2
        v.append(n)

for f in range(0, 10):
    print('N[%d] = %d' %(f, v[f]))
