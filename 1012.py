#include<stdio.h>

x = input().split()

a, b, c = float(x[0]), float(x[1]), float(x[2])

print('TRIANGULO: %.3f' %((a * c) / 2))
print('CIRCULO: %.3f' %( 3.14159 * (c ** 2)))
print('TRAPEZIO: %.3f' %(((a + b) * c) / 2))
print('QUADRADO: %.3f' %( b ** 2))
print('RETANGULO: %.3f' %(a * b))

