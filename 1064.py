#include<stdio.h>

aux = 0
media = 0

for x in range(0, 6):
    n = float(input())
    if n > 0:
        aux+= 1
        media += n

print('%d valores positivos\n%.1f' %(aux, (media / aux)))

    