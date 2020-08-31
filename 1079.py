#include<stdio.h>

n = int(input())

for x in range(0, n):
    x = input().split()
    n1, n2, n3 = float(x[0]), float(x[1]), float(x[2])
    med = (((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10)
    print('%.1f' %(med))