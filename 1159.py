#include<stdio.h>



while True:
    n = int(input())

    if n == 0:
        break
    
    if (n % 2) != 0:
        n += 1
    
    aux = n
    n = 0

    for d in range(aux, (aux + (10)), 2):
        n += d
    
    print(n)
