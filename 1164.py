#include<stdio.h>

n = int(input())

for i in range(0, n):
    cont = 0
    y = int(input())

    for x in range(1, y):
        if (y % x) == 0:
            cont += x
    
    if cont == y:
        print('%d eh perfeito' %(y))
    else:
        print('%d nao eh perfeito' %(y))