#include<stdio.h>

t = int(input())

for c in range(0, t):
    n = input().split()

    x, y = int(n[0]), int(n[1])

    if y == 0:
        print('divisao impossivel')
    else:
        print('%.1f' %(x / y))