#include<stdio.h>
aux = 0
t = 0
while True:

    n = float(input())

    if n >= 0 and n <= 10:
        aux += n
        t += 1
    else:
        print('nota invalida')

    if t == 2:
        print('media = %.2f' %(aux / 2))
        break