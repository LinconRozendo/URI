#include<stdio.h>

x = float(input())



n = [0, 0, 0, 0, 0, 0]

for c in range(1000000):
    if(x > 0):
        if (x - 100) >= 100 or (x - 100) >= 0:
            x -= 100
            n[0] += 1
        else:
            if (x - 50) >= 50  or (x - 50) >= 0:
                x -= 50
                n[1] += 1
            else:
                if (x - 20) >= 20 or (x - 20) >= 0:
                    x -= 20
                    n[2] += 1
                else:
                    if(x - 10) >= 10 or (x - 10) >= 0:
                        x -= 10
                        n[3] += 1
                    else:
                        if(x - 5) >= 5 or (x - 5) >= 0:
                            x -= 5
                            n[4] += 1
                        else:
                            if(x - 2) >= 2 or (x - 2) >= 0:
                                x -= 2
                                n[5] += 1
                            else:                                
                                break
print('NOTAS:')
print('%d nota(s) de R$ 100.00' %(n[0]))
print('%d nota(s) de R$ 50.00' %(n[1]))
print('%d nota(s) de R$ 20.00' %(n[2]))
print('%d nota(s) de R$ 10.00' %(n[3]))
print('%d nota(s) de R$ 5.00' %(n[4]))
print('%d nota(s) de R$ 2.00' %(n[5]))

n = [0, 0, 0, 0, 0, 0]

x = int(x * 100)
for c in range(1000000):
    if(x > 0):
        if (x - 100) >= 100 or (x - 100) >= 0:
            x -= 100
            n[0] += 1        
        else:
            if (x - 50) >= 50  or (x - 50) >= 0:
                x -= 50
                n[1] += 1
            else:
                if (x - 25) >= 25 or (x - 25) >= 0:
                    x -= 25
                    n[2] += 1
                else:
                    if(x - 10) >= 10 or (x - 10) >= 0:
                        x -= 10
                        n[3] += 1
                    else:
                        if(x - 5) >= 5 or (x - 5) >= 0:
                            x -= 5
                            n[4] += 1
                        else:
                            if(x - 1) >= 1 or (x - 1) >= 0:
                                x -= 1
                                n[5] += 1
                            else:
                                break


print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' %(n[0]))
print('%d moeda(s) de R$ 0.50' %(n[1]))
print('%d moeda(s) de R$ 0.25' %(n[2]))
print('%d moeda(s) de R$ 0.10' %(n[3]))
print('%d moeda(s) de R$ 0.05' %(n[4]))
print('%d moeda(s) de R$ 0.01' %(n[5]))





