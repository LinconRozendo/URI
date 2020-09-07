#include<stdio.h>

x = int(input())
aux = x
cont = 1
while True:
    z = int(input())

    if z > x:
        break

for c in range(0, z):
    if x <= z:
        x += (aux + c)
        cont += 1

    

print(cont)