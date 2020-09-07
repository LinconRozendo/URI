#include<stdio.h>

n = int(input())

aux = 0

for i in range(0, 1000):
    print('N[%d] = %d' %(i, aux))
    if aux == (n - 1):
        aux = 0
    else:
        aux += 1
    
    