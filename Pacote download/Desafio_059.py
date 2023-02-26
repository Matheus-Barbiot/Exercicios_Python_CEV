from time import sleep

#ESCOLHENDO OS NÚMEROS.

n1 = int (input ('Primeiro número: '))
n2 = int (input ('Segundo número: '))

op = 0
#O MAIOR NÚMERO.

maior = 0

if n1 >= n2:
    maior = n1

elif n2 >= n1:
    maior = n2

#MENU DE OPÇÕES.

while op != 5:
    print ('''
    [ 1 ] Soma
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] finalizar
        ''')
    op = int (input ('Digite sua opção: '))
    print (' ')

#CONDIÇÕES.
    sleep (0.5)
    if op == 1:
        print (f'''{"•="*30}
A soma entre {n1} e {n2} é {n1+n2}
{"•="*30}
''')

    if op == 2:
        print (f'''{"•="*30}
A multiplicação de {n1} e {n2} é {n1*n2}
{"•="*30}
''')

    if op == 3:
        print (f'''{"•="*30}
O maior número escolhido foi {maior}
{"•="*30}
''')

    if op == 4:
        print (f'{"•="*30}')
        n1 = int (input ('Primeiro número: '))
        n2 = int (input ('Segundo número: '))
        print (f'{"•="*30}')

    if op >= 6:
                print (f'''{"•="*30}
Número inválido!
{"•="*30}
''')
    sleep (1)
#FINALIZAÇÃO.   
     
print ('Programa finalizado, volte sempre!')