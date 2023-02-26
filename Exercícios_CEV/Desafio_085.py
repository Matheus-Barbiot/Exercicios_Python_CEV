      #INICIO
SEPARADOR = [[], []]
for C in range (1, 8):
    VALOR = int (input (f'Digite o {C}ª valor: '))

      #CONDICIONADOR.    
    if VALOR % 2 == 0:
        SEPARADOR[0].append(VALOR)
    else:
        SEPARADOR[1].append(VALOR)

      #ORDENADOR.      
SEPARADOR[0].sort()
SEPARADOR[1].sort()

      #MOSTRAR.
print (f'Valores pares: {SEPARADOR[0]}.')
print (f'Valores ímpares: {SEPARADOR[1]}.')