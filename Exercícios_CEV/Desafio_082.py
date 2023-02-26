lista = []
pares = []
impares = []

while True:
    valor = int (input ('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    op = str (input ('Continuar? '))
    
    if op == 'não':
        break

print (f'Você digitou os números: {lista}')
print (f'Pares digitados: {pares}')
print (f'Impares digitados: {impares}')