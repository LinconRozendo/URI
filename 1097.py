#include<stdio.h>


aux = 0
aux_aux = 0

for x in range(0, 11, 1):
    for y in range(1, 4):
        if x == 0 or x == 5:
            print('I=%d J=%d' %(aux_aux + aux, (y + aux)))
        else:
            if x == 10:
               print('I=%.0f J=%.0f' %(aux_aux + aux, (y + aux)))
            else: 
                print('I=%.1f J=%.1f' %(aux_aux + aux, (y + aux)))
            
    
    aux += 0.2
    
