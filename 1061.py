#include<stdio.h>

d1 = input().split()
i  = input().split(':')
d2 = input().split()
f  = input().split(':')

dia1 = int(d1[1])
hi, mi, si = int(i[0]), int(i[1]), int(i[2])
dia2 = int(d2[1])
hf, mf, sf = int(f[0]), int(f[1]), int(f[2])

dia = 0
hora = 0 
min = 0
sec = 0


dia = dia2 - dia1

if hf >= hi and mf >= mi and sf >= si:
    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hf - hi))
    print('%d minuto(s)' %(mf - mi))
    print('%d segundo(s)' %(sf - si))

if hf >= hi and mf >= mi and sf < si:
    hora = hf - hi
    min = mf - mi - 1
    sec = 60 - (si - sf)
    if (min) < 0:
        min = (mf - mi - 1) + 60
        hora = (hf - hi - 1)
        if (hora) < 0:
            hora = (hf - hi - 1) + 24
            dia -= 1
    
    if dia < 0:
        dia = 0

    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hora))
    print('%d minuto(s)' %(min))
    print('%d segundo(s)' %(sec))

if hf >= hi and mf < mi and sf < si:
    hora = hf - hi - 1
    min = 60 - (mi - mf + 1)
    sec = 60 - (si - sf)
    if (hora) < 0:
            hora = (hf - hi - 1) + 24
            dia -= 1

    if dia < 0:
        dia = 0

    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hora))
    print('%d minuto(s)' %(min))
    print('%d segundo(s)' %(sec))

if hf < hi and mf < mi and sf < si:
    hora = 24 - (hi - hf + 1)
    min = 60 - (mi - mf + 1)
    sec = 60 - (si - sf)
    dia -= 1
    
    if dia < 0:
        dia = 0

    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hora))
    print('%d minuto(s)' %(min))
    print('%d segundo(s)' %(sec))

if hf < hi  and mf >= mi and sf >= si:
    hora = 24 - (hi - hf)
    min = mf - mi
    sec = sf - si
    dia -= 1

    if dia < 0:
        dia = 0

    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hora))
    print('%d minuto(s)' %(min))
    print('%d segundo(s)' %(sec))

if hf < hi and mf < mi and sf >= si:
    hora = 24 - (hi - hf + 1)
    min = 60 - (mi - mf)
    sec = sf - si
    dia -= 1

    if dia < 0:
        dia = 0

    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hora))
    print('%d minuto(s)' %(min))
    print('%d segundo(s)' %(sec))

if hf < hi and mf >= mi and sf < si:
    hora = 24 - (hi - hf)
    min = mf - mi
    sec = 60 - (si - sf)
    dia -= 1

    if dia < 0:
        dia = 0

    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hora))
    print('%d minuto(s)' %(min))
    print('%d segundo(s)' %(sec))

if hf >= hi and mf < mi and sf >= si:
    hora = hf - hi - 1
    min = 60 - (mi - mf)
    sec = sf - si
    if (hora) < 0:
            hora = (hf - hi - 1) + 24
            dia -= 1
    
    if dia < 0:
        dia = 0
        
    print('%d dia(s)' %(dia))
    print('%d hora(s)' %(hora))
    print('%d minuto(s)' %(min))
    print('%d segundo(s)' %(sec))

