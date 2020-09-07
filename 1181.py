#include<stdio.h>

matriz = []
linha = int(input())
op = input()
ope = 0

while True:
    aux = []
    for j in range(0, 12):
        aux.append(float(input()))
    
    matriz.append(aux)

    if len(matriz) == 12:
        break

if op == 'S':
    for i in range(0, 12):
        ope += matriz[linha][i]

if op == 'M':
    for i in range(0, 12):
        ope += matriz[linha][i]
    ope /= 3
    
print(matriz)
print('%.1f'%(ope))
