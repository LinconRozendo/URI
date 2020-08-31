#include<stdio.h>

n = input().split()

x, y = int(n[0]), int(n[1])

for c in range(0, 24):
    x += 1

    if x == 24:
       x = 0
    if x == y:
        c += 1
        print('O JOGO DUROU %d HORA(S)' %(c))
        break