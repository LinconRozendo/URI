#include<stdio.h>

x = int(input())


a = int(x / 365)
m_aux = int(x - (a * 365))
m = int(m_aux / 30)
d = int(m_aux - (m * 30))


print('%d ano(s)' %(a))
print('%d mes(es)' %(m))
print('%d dia(s)' %(d))


