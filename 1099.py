#include<stdio.h>

t = int(input())

for d in range(0, t):
    num = input().split()
    x, y = int(num[0]), int(num[1])

    v = 0

    if y < x:
        for n in range((x - 1), y, - 1):
            if (n % 2) != 0:
                v += n

    else:
        for n in range(x + 1, y):
            if (n % 2) != 0:
                v += n

    print(v)