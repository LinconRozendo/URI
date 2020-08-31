#include<stdio.h>

aux = 0
lista = []
while True:
    n = input().split()
    n1, n2 = int(n[0]), int(n[1])

    if n1 <= 0 or n2 <= 0:
        break
    else:
        aux = 0
        if n2 > n1:
            aux = n1
            n1 = n2
            n2 = aux
            aux = 0
 
        for x in range(n2, (n1 + 1)):
            print(str(x) + " ", end='')
            aux += x

        print('Sum=%d' %(aux))