#include<stdio.h>

x = float(input())


if x > 100 or x < 0:
    print('Fora de intervalo')
else:
    if x >= 0 and x <= 25:
        print('Intervalo [0,25]')
    else:
        if x > 25 and x <= 50:
            print('Intervalo (25,50]')
        else:
            if x > 50 and x <= 75:
                print('Intervalo (50,75]')
            else:
                print('Intervalo (75,100]')

