num = int (input ('Digite um número inteiro qualquer: '))
print ('''Escolha uma das opções a seguir para conversão:

1 - Binario.
2 - Octal.
3 - hexadecimal.
''')

opção = int (input ('Sua escolha: '))

if opção == 1:
    print (f'''\033[32m
O número {num} convertido para binário: {bin (num)[2:]}\033[m''')

elif opção == 2:
    print (f'''\033[32m
O número {num} convertido para octal: {oct (num)[2:]}\033[m''')

elif opção == 3:
    print (f'''\033[32m
O número {num} convertido para hexadecimal: {hex (num)[2:]}\033[m''')

else:
    print ('\033[31mNÚMERO INVALIDO!\033[m')