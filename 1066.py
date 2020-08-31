#include<stdio.h>

par = 0
impar = 0
pos = 0
neg = 0

for x in range(0, 5):
    n = int(input())
    if (n % 2) == 0:
        par += 1
    else:
        impar += 1
    
    if n > 0:
        pos += 1
    else:
        if n < 0:
            neg += 1

print('%d valor(es) par(es)' %(par))
print('%d valor(es) impar(es)' %(impar))
print('%d valor(es) positivo(s)' %(pos))
print('%d valor(es) negativo(s)' %(neg))
