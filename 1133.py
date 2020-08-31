#include<stdio.h>

x = int(input())
y = int(input())

aux = 0

if x > y:
    aux = y
    y = x
    x = aux

for c in range(x + 1, (y)):

    if (c % 5) == 2 or (c % 5) == 3:
        print(c)

