#include<stdio.h>

n = int(input())

for c in range(0, n):
    n = input().split()
    x, y = int(n[0]), int(n[1])

    if (x % 2) == 0:
        x += 1
    
    aux = x
    x = 0

    for d in range(aux, (aux + (y * 2)), 2):
        x += d
    
    print(x)
