#include<stdio.h>

i = 0
g = 0
e = 0
j = 0
t = 0

while True:

    n = input().split()
    n1, n2 = int(n[0]), int(n[1])
    j += 1

    if n1 > n2:
        i += 1
    
    if n2 > n1:
        g += 1
    
    if n2 == n1:
        e += 1
    
    while True:
        t = int(input('Novo grenal (1-sim 2-nao)\n'))
        
        if t == 1:
            break

        if t == 2:
            break
    
    if t == 2:
        print('%d grenais' %(j))
        print('Inter:%d' %(i))
        print('Gremio:%d' %(g))
        print('Empates:%d' %(e))

        if(i > g):
            print('Inter venceu mais')
        else:
            if i < g:
                print('Gremio venceu mais')
            else:
                print('Nao houve vencedor')
        break

