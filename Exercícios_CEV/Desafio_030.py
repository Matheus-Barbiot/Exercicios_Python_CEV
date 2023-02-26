from time import sleep

#COMEÇO:
n = int (input ('Digite um número qualquer: '))
d = n % 2

#SUSPENCE:
print ('PROCESSANDO. . .')
sleep (2)

#RESULTADO:
if d == 1:
    print (f'O número {n} é ÍMPAR.')
else:
    print (f'O número {n} é PAR.')