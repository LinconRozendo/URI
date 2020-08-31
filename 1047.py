#include<stdio.h>

n = input().split()

hi, mi, hf, mf = int(n[0]), int(n[1]), int(n[2]), int(n[3])

mi_aux = mi
mx = 0
hx = 0

for c in range(0, 1440):
    if mi == mf and hi == hf:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
        break

    mi += 1

    mx += 1
    
    if mi == 60:
       mi = 0
       hi += 1
    if mx == 60:
       mx = 0
       hx += 1
    if mi == mf and hi == hf:
        print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(hx, mx))
        break