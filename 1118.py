#include<stdio.h>
aux = 0
t = 0
c = 0
while True:

    n = float(input())

    if n >= 0 and n <= 10:
        aux += n
        t += 1
    else:
        print('nota invalida')

    if t == 2:
        print('media = %.2f' %(aux / 2))
        aux = 0
        t = 0
        while True:
            c = int(input('novo calculo (1-sim 2-nao)\n'))

            if c == 1:
                break
            if c == 2:
                break
    if c == 2:
        break