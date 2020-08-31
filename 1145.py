#include<stdio.h>

n = input().split()

n1, n2 = int(n[0]), int(n[1])
t = 0

for x in range(1, n2, n1):
    t = 0
    while True:
        if t == (n1 - 1) and (x + t) <= n2:
            print('%d'%(x + t))
            break
        else:
            if (x + t) > n2:
                break

            print('%d '%(x + t), end='')
            t += 1
        

    