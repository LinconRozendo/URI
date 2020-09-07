#include<stdio.h>

v = []

x = 0
aux = 0
aux_2 = 0
for i in range(0, 100):
    if i == 0:
        v.append(0)
        x += 1
    else:
        if i == 1:
            aux = 0
            x = 1
            x += aux
            v.append(x)
        else:
            aux_2 = x
            x += aux
            aux = aux_2
            v.append(x)

n = int(input())

for j in range(0, n):
    n = int(input())
    print('Fib(%d) = %d' %(n, v[n]))

    
        
