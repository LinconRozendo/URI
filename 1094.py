#include<stdio.h>

n = int(input())

qt = 0
qc = 0
qr = 0
qs = 0

for x in range(0, n):
    d = input().split()
    q, c = int(d[0]), d[1]
    qt += q

    if c == 'C':
        qc += q
    if c == 'R':
        qr += q
    if c == 'S':
        qs += q

print('Total: %d cobaias' %(qt))
print('Total de coelhos: %d' %(qc))  
print('Total de ratos: %d' %(qr))
print('Total de sapos: %d' %(qs))
print('Percentual de coelhos: %.2f %%' %((qc / qt) * 100))
print('Percentual de ratos: %.2f %%' %((qr / qt) * 100))
print('Percentual de sapos: %.2f %%' %((qs / qt) * 100))
