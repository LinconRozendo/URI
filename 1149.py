#include<stdio.h>

n = input().split()

aux = 1
if int(n[aux]) <= 0:
    while True:
        if int(n[aux]) <= 0:
            aux+= 1
        if int(n[aux]) > 0:
            break

a, n, aux = int(n[0]), int(n[aux]), int(n[0])

for x in range(1, n):
    a += (aux + x)

print(a)


