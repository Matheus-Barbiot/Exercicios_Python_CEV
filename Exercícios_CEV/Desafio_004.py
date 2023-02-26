#DESAFIO 004

a = input ('Digite algo: ')


print ('Qual o seu tipo primitivo?', type(a))

print ('É alfa-numérico? {}'.format (a.isalnum()))

print ('É alfabético? {}'.format (a.isalpha()))

print ('É numérico? {}'.format (a.isdigit()))

print ('Possui apenas letras minúsculas? {}'.format (a.islower()))

print ('Consiste em apenas espaços? {}'.format (a.isspace()))

print ('A primeira letra está maiúscula? {}'.format (a.istitle()))

print ('Todas as letras estão em maiúsculo? {}'.format (a.isupper()))
