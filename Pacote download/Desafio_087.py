#        INICIO.
MATRIZ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
SOMA_PARES = 0
SOMA_COLUNA_3 = 0
MAIOR_LINHA_2 = 0

#        FORMAÇÃO_DA_MATRIZ.
for L in range(0, 3):
    for C in range(0, 3):
        MATRIZ[L][C] = int (input ('Digite um valor: '))
        
        if MATRIZ[L][C] % 2 == 0:
            SOMA_PARES += MATRIZ[L][C]
        
        if C == 2:
            SOMA_COLUNA_3 += MATRIZ[L][C]
                     
#        VISUALIZAÇÃO_DA_MATRIZ.
print ('=' * 30)
for L in range(0, 3):
    for C in range(0, 3):
        print (f'[ {MATRIZ[L][C]} ]', end = ' ')
    print ()

#        FINALIZANDO_PROGRAMA.
print ('=' * 30)
print (f'A soma dos pares é: {SOMA_PARES}')
print (f'A soma dos valores da terceira coluna é: {SOMA_COLUNA_3}.')
for C in range(0, 3):
    if C == 0:
        MAIOR_LINHA_2 = MATRIZ[1][C]
    else:
        if MATRIZ[1][C] > MAIOR_LINHA_2:
            MAIOR_LINHA_2 = MATRIZ[1][C]
print (f'O Maior número da segunda linha é: {MAIOR_LINHA_2}.')
    