#include<stdio.h>

x = input().split()

n1, n2 = int(x[0]), int(x[1])


if n1 == 1:
    n2 *= 4.0

if n1 == 2:
    n2 *= 4.5

if n1 == 3:
    n2 *= 5.0

if n1 == 4:
    n2 *= 2.0

if n1 == 5:
    n2 *= 1.5

print('Total: R$ %.2f' %(n2))