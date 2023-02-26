
#            FUNÇÃO QUE DEFINE O MAIOR
def maior(num):
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print (f'O maior número é {maior}.')

#            GAVETA DE VARIAVEIS.
NUMEROS_ = []

#            LEITOR DE VALORES
while True:
    NUM_ = int (input ('Digite um valor: '))
    NUMEROS_.append(NUM_)
    print ('-' * 30)
    
    CTN_ = str (input ('Deseja continuar? ')).upper()[0]
    if not CTN_ in 'NS':
        while CTN_ not in 'NS':
            CTN_ = str(input ('Valor invalido, deseja continuar? ')).upper()[0]
    if CTN_ == 'N':
        break
    print ('-' * 30)
   
#             FINALIZAÇÃO.
print ('=' * 40)
maior (NUMEROS_)
