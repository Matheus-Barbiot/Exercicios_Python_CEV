from random import randint
from time import sleep

def sortear(list):
    print ('Os valores sorteados foram: ', end = ' ')
    for n in range (0, 5):
        num = randint(0, 10)
        list.append(num)
    for num in list:
        print (f'{num}', end = ' ', flush = True)
        sleep(0.5)
    print ()
        
    

def somapar(list):
    soma = 0
    for n in list:
        if n % 2 == 0:
            soma += n
    print (f'A soma dos números pares foi: ', end = ' ', flush = True)
    sleep (0.3)
    print (f'{soma}')
    print ()

lista = []
sortear(lista)
somapar(lista)




        