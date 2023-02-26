from datetime import date

ano = int (input ('Digite um ano, digite 0 para saber seu ano:  '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano de {ano} é um ano bisexto.')
else:
    print (f'O ano de {ano} não é um ano bisexto.')
