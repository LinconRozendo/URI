#include<stdio.h>

v = []

for i in range(0, 10):
    v.append(int(input()))

    if v[i] <= 0:
        v[i] = 1
    
for i in range(0, 10):
    print('X[%d] = %d' %(i, v[i]))