#include<stdio.h>

x = input().split()
y = input().split()

n1, n2, n3 = int(x[0]), int(x[1]), float(x[2])
n4, n5, n6 = int(y[0]), int(y[1]), float(y[2])

print('VALOR A PAGAR: R$ %.2f' %((n2 * n3) + n5 * n6))