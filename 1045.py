#include<stdio.h>

n = input().split()

n1, n2, n3 = float(n[0]), float(n[1]), float(n[2])

a = n1
b = n2 
c = n3

if n1 >= n2 and n1 >= n3:
    a = n1
    if n2 >= n3:
        b = n2
        c = n3
    else:
        b = n3
        c = n2

if n2 >= n1 and n2 >= n3:
    a = n2
    if n1 > n3:
        b = n1
        c = n3
    else:
        b = n3
        c = n1

if n3 >= n1 and n3 >= n2:
    a = n3
    if n1 >= n2:
        b = n1
        c = n2
    else:
        b = n2
        c = n1

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == ((b ** 2) + (c ** 2)):
        print('TRIANGULO RETANGULO')
    if (a ** 2) > ((b ** 2) + (c ** 2)):
        print('TRIANGULO OBTUSANGULO')
    if (a ** 2) < ((b ** 2) + (c ** 2)):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    else:
        if a == b or b == c or a == c:
            print('TRIANGULO ISOSCELES')
