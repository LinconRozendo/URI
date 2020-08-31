#include<stdio.h>

x = int(input())
y = int(input())

aux = 0
soma = 0

if x > y:
    aux = y
    y = x
    x = aux

for c in range(x, (y + 1)):

    if (c % 13) != 0:
        soma += c

print(soma)