#include<stdio.h>

n = int(input())

for x in range(1, (n+1)):
    print('%d %d %d' %((x), (x ** 2), (x ** 3)))
    print('%d %d %d' %((x), ((x ** 2) + 1), ((x ** 3) + 1)))
