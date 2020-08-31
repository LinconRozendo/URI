#include<stdio.h>

x = int(input())


m = int(x / 60)
s = int(x - (m * 60))
h = int(m / 60)
m -= (h * 60)

print('%d:%d:%d' %(h, m, s))


