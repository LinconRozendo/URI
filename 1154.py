#include<stdio.h>

t = 0
c = 0

while True:
    n = int(input())

    if n < 0:
        print('%.2f' %(t / c))
        break
    else:
        t += n
        c += 1