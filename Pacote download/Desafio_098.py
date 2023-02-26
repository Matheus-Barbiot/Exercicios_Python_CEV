from time import sleep

#            FUNCIONALIDADE CONTADORA.
def contador(inicio, fim, passo):
    count = inicio
    print (f'A contagem de {inicio} até {fim} pulando de {passo} em {passo} é:')

    if inicio > fim:
        while not count <= fim:
            print (f'{count} →', end = ' ', flush = True)
            sleep(0.5)
            count -= passo
        print ('FIM!')
    
    else:
        while count < fim:
            print (f'{count} →', end = ' ', flush = True)
            sleep(0.5)
            count += passo
        print ('FIM!')


#            DEMONSTRAÇÃO DO PROGRAMA.
contador(3, 40, 5)
print ('=' * 50)
contador(50, 3, 7)
print ('=' * 50)

#            ESCOLHA DO USUÁRIO.
INICIO_ = int (input ('Digite o início: '))
FIM_ = int (input ('Digite o fim: '))
PASSO_ = int (input ('Digite de quanto em quanto irá pular: '))

#            NUMERO NEGATIVO NO PASSO.
if PASSO_ < 0:
    PASSO_ *= -1

#            FINALIZANDO.
print ('-' * 30)
contador(1, 10)
