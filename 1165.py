#include<stdio.h>

n = int(input())

for i in range(0, n):
    cont = 0
    y = int(input())

    for x in range(1, y):
        if (y % x) == 0:
            cont += 1
    
    if cont == 1:
        print('%d eh primo' %(y))
    else:
        print('%d nao eh primo' %(y))