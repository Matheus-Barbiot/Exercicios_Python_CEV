n1 = int (input ('Digite um número: '))
print ('=' * 50)

soma = n1
count = 1
continuar = 's'
maior = n1
menor = n1

while continuar != 'n':
    n1 = int (input ('Digite um número: '))
    print ('=' * 50)
    continuar = str (input ('Deseja continuar? [s/n] '))
    print ('=' * 50)
    
    if n1 >= maior:
        maior = n1
    if n1 <= menor:
        menor = n1

    soma += n1
    count += 1

print (f'A média de números é {soma/count}')
print (f'O maior número digitado foi {maior}')
print (f'O menor número digitado foi {menor}')
