#include<stdio.h>

n = input().split()

x, y = float(n[0]), float(n[1])

if x == 0 and y == 0:
    print('Origem')
else:
    if x == 0 and y != 0:
        print('Eixo Y')
    else:
        if x != 0 and y == 0:
            print('Eixo X')
        else:
            if x > 0 and y > 0:
                print('Q1')
            else:
                if x < 0 and y > 0:
                    print('Q2')
                else:
                    if x < 0 and y < 0:
                        print('Q3')
                    else:
                        print('Q4')


