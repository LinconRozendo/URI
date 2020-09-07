#include<stdio.h>

while True:

    n = int(input())

    if n == 0:
        break

    for x in range(1, (n + 1), 1):
        if x == n:
            print(x)
        else:
            print(str(x) + ' ', end='')