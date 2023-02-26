from random import randrange
from time import sleep

#Cores:
final = str ('\033[m')
yellow = str ('\033[33m')
blue = str ('\033[34m')
red = str ('\033[31m')
green = str ('\033[32m')
purple = str ('\033[35m')

#Começo do jogo:
print (f'{yellow}-='*28)
print ('VOU PENSAR ENTRE UM NÚMERO ENTRE 0 E 5, TENTE ADIVINHAR!')
print (f'=-'*28)

#Numero escolhido:
n = int (randrange (0, 6))
nr = int (input (f'{blue}adivinhe o numero: '))
print (' ')
print (f'PROCESSANDO. . .{final}')
sleep (2)
print (' ')

#Condições:
if nr >=6:
    print (f'{red}ESTE NÚMERO É INVALIDO!{final}')
else:
    if nr == n:
        print (f'{green}PARABÉNS, VOCÊ ACERTOU! EU PENSEI EM {nr}! {final}')
    else:
        print (f'{purple}VOCÊ ERROU! EU NÃO PENSEI EM {nr}, EU PENSEI EM {n}! {final}')
