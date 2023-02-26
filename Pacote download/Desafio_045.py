from random import randrange 
from time import sleep


#CORES

vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[93m'
cinza = '\033[90m'
final = '\033[m'

#OPÇÕES
print (f'''{amarelo}SUAS OPÇÕES:
{"-="*30}
1 - Pedra
2 - Papel
3 - Tesoura
{"-="*30} {final}
''')

#ESCOLHA
op = int (input (f'{cinza}Sua escolha: '))
opb = randrange (1, 3)

if op >= 4:
    print (f'{vermelho}NUMERO INVALIDO!!{final}')
    
else:
#JO KEN PO
    print (' ')
    print (f'{amarelo}JO')
    sleep (0.8)

    print ('KEN')
    sleep (0.8)

    print (f'PÔ!!!{final}')
    sleep (0.5)
    print (' ')
    
#FORMAS DE VENCER
    if op == 1 and opb == 3:
        print ('Pedra X Tesoura')
        print (f'{verde}VOCÊ VENCEU!!{final}')

    elif op == 2 and opb == 1:
        print ('Papel X Pedra')
        print (f'{verde}VOCÊ VENCEU!!{final}')

    elif op == 3 and opb == 2:
        print ('Tesoura X Papel')
        print (f'{verde}VOCÊ VENCEU!!{final}')


#FORMAS DE PERDER
    elif op == 1 and opb == 2:
        print ('Pedra X Papel')
        print (f'{vermelho}VOCÊ PERDEU!!{final}')
    
    elif op == 2 and opb == 3:
        print ('Papel X Tesoura')
        print (f'{vermelho}VOCÊ PERDEU!!{final}')

    elif op == 3 and opb == 1:
        print ('Tesoura X Pedra')
        print (f'{vermelho}VOCÊ PERDEU!!{final}')
        
#EMPATE
    if op == opb:
        print ('EMPATE!!!')