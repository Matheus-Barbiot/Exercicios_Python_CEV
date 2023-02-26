count = 0
n = int (input ('Digite um número: '))

for calc in range (1, n+1):
    if n % calc >= 1:
        print (f'{calc}', end=' ')
    else:
        count = count + 1
        print (f'\033[32m{calc}\033[m', end=' ')
print (f'\nO número {n} foi dividido {count} vezes')
if count == 2:
    print ('Ele é um número primo.')
else:
    print ('Ele não é um número primo.')
