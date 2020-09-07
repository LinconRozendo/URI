#include<stdio.h>

s = 1
aux = 2

for x in range(3, 40, 2):
    s+= (x / aux)
    aux *= 2

print('%.2f' %(s))