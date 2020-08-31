#include<stdio.h>

n = input().split()

x,y = int(n[0]), int(n[1])

if x > y:
    if x % y == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if y % x == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')