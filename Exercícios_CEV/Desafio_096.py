#        INÍCIO.
def area(a, b):
    print (f'A area do terreno é {a*b}m²')
    

#        INFORMAÇÕES.
print ('-' * 65)
print (f'{"CALCULO DE TERRENO":^60}')
print ('-' * 65)

NUM_1 = int (input ('Digite a altura: '))
NUM_2 = int (input ('Digite a largura: '))

#        FINALIZANDO.
print (f'•{"=" * 30}•')
area(NUM_1, NUM_2)