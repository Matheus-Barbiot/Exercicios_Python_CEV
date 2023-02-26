n1 = int (input ('Digite um número: '))
soma = n1
count = 0

while n1 != 999:
    n1 = int (input ('Digite um número: '))
    soma += n1
    count += 1
print (f'Você digitou {count} números e a soma é {soma-999}.')