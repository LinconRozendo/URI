#include<stdio.h>

v = []

for i in range(0, 20):
    v.append(int(input()))

v.reverse()

for f in range(0, 20):
    print('N[%d] = %d' %(f, v[f]))