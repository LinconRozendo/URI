#include<stdio.h>

n = float(input())

aux = 0

if n > 2000:
    if (n - 2000) > 1000:
        aux = (1000 * 0.08)
    else:
        aux = (n - 2000) * 0.08

    if n > 3000:
        if (n - 3000) > 1500:
            aux += (1500 * 0.18)
        else:
            aux += (n - 3000) * 0.18

    if n > 4500:
        aux += (n - 4500) * 0.28

    print('R$ %.2f' %(aux))
else:
    print('Isento')
