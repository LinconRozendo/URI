#include<stdio.h>

n = input().split()

n1, n2, n3, n4 = float(n[0]), float(n[1]), float(n[2]), float(n[3])

media = (((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10 )

if media >= 7:
    print('Media: %.1f' %(media))
    print('Aluno aprovado.')
else:
    if media < 5:
        print('Media: %.1f' %(media))
        print('Aluno reprovado.')
    else:
        print('Media: %.1f' %(media))
        print('Aluno em exame.')
        nota_exame = float(input())
        media = (media + nota_exame) / 2
        print('Nota do exame: %.1f' %(nota_exame))

        if nota_exame >= 5:
            print('Aluno aprovado.')
            print('Media final: %.1f' %(media))
        else:
            print('Aluno reprovado.')
            print('Media final: %.1f' %(media))