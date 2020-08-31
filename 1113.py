#include<stdio.h>

while True:
    n = input().split()
    n1, n2 = int(n[0]), int(n[1])

    if n1 == n2:
        break
    else:
        if n1 > n2:
            print('Decrescente')
        else:
            print('Crescente')