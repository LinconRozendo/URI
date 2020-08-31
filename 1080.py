#include<stdio.h>

t = 0
p = 0

for x in range(0, 100):
    n = int(input())

    if n > t:
        t = n
        p = x + 1

print(t)
print(p)