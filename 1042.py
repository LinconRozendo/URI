#include<stdio.h>

n = input().split()

n1, n2, n3 = int(n[0]), int(n[1]), int(n[2])

p1 = n1
p2 = n2 
p3 = n3

if n1 < n2 and n1 < n3:
    p1 = n1
    if n2 < n3:
        p2 = n2
        p3 = n3
    else:
        p2 = n3
        p3 = n2

if n2 < n1 and n2 < n3:
    p1 = n2
    if n1 < n3:
        p2 = n1
        p3 = n3
    else:
        p2 = n3
        p3 = n1

if n3 < n1 and n3 < n2:
    p1 = n3
    if n1 < n2:
        p2 = n1
        p3 = n2
    else:
        p2 = n2
        p3 = n1


print('%d\n%d\n%d\n\n%d\n%d\n%d' %(p1, p2, p3, n1, n2, n3))