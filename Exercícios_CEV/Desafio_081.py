lista = []
count = 0
op = 'sim'

while op != 'não':
    valor = int (input ('Digite um valor: '))
    lista.append(valor)
    count += 1
    op = str (input ('Continuar? '))
five = 5 in lista
print (f'Os valores digitados foram: {lista}')
print (f'Você digitou {count} valores.')
lista.sort()
lista.reverse()
print (f'Os valores em ordem decrescente são {lista}')

if five == True:
    print ('O número 5 foi encontrado com sucesso.')
else:
    print ('O número 5 não foi encontrado.')