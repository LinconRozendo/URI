#include<stdio.h>

n = float(input())

if n <= 400:
    print('Novo salario: %.2f' %(n + (n * 0.15)))
    print('Reajuste ganho: %.2f' %(n * 0.15))
    print('Em percentual: 15 %')

if n > 400 and n <= 800:
    print('Novo salario: %.2f' %(n + (n * 0.12)))
    print('Reajuste ganho: %.2f' %(n * 0.12))
    print('Em percentual: 12 %')

if n > 800 and n <= 1200:
    print('Novo salario: %.2f' %(n + (n * 0.10)))
    print('Reajuste ganho: %.2f' %(n * 0.10))
    print('Em percentual: 10 %')

if n > 1200 and n <= 2000:
    print('Novo salario: %.2f' %(n + (n * 0.07)))
    print('Reajuste ganho: %.2f' %(n * 0.07))
    print('Em percentual: 7 %')

if n > 2000:
    print('Novo salario: %.2f' %(n + (n * 0.04)))
    print('Reajuste ganho: %.2f' %(n * 0.04))
    print('Em percentual: 4 %')

    






