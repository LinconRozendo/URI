#include<stdio.h>

while True:

    n = input().split()

    x, y = int(n[0]), int(n[1])

    if x == 0 or y == 0:
        break
    else:
        if x > 0 and y > 0:
            print('primeiro')

        if x < 0 and y > 0:
            print('segundo')
        
        if x < 0 and y < 0:
            print('terceiro')

        if x > 0 and y < 0:
            print('quarto')