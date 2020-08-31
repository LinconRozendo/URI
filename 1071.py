#include<stdio.h>

x = int(input())
y = int(input())

v = 0

if y < x:
    for n in range((x - 1), y, - 1):
        if (n % 2) != 0:
            v += n

else:
    for n in range(x, y):
        if (n % 2) != 0:
            v += n



print(v)