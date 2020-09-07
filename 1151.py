#include<stdio.h>

n = int(input())

aux = 0
aux_2 = 0
c = 0

for x in range(1, (n + 1)):
    if x == 1:
        print(str(c) + ' ', end='')
        c += 1
    else:
        if x == (n):
            c += aux
            print(c)
        else:
            if x == 3:
                aux_2 = c
                aux = 0
                c += aux
                print(str(c) + ' ', end='')
                aux = aux_2
            else:
                aux_2 = c
                c += aux
                print(str(c) + ' ', end='')
                aux = aux_2
            

