#include<stdio.h>

n = int(input())

v = list(map(int, input().split()))

cont = 10000
pos = 0

for i in range(0, n):
    if v[i] < cont:
        cont = v[i]
        pos = i

print('Menor valor: %d' %(cont))
print('Posicao: %d' %(pos))