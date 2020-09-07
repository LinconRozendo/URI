#include<stdio.h>

par = []
impar = []

tPar = 0
tImpar = 0

for i in range(0, 15):
    n = int(input())

    if (n % 2) == 0:
        par.append(n)
        tPar += 1
    else:
        impar.append(n)
        tImpar += 1

    if tPar == 5:
        for j in range(0, tPar):
            print('par[%d] = %d' %(j , par[j]))

        del par [:]
        tPar = 0
    
    if tImpar == 5:
        for j in range(0, tImpar):
            print('impar[%d] = %d' %(j , impar[j]))

        del impar [:]
        tImpar = 0
    
    if i == 14:
        for j in range(0, tImpar):
            print('impar[%d] = %d' %(j , impar[j]))

        for j in range(0, tPar):
            print('par[%d] = %d' %(j , par[j]))
    
