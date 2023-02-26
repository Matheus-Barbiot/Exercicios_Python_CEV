loja = (' ',
'Caneta nanquim', 12.50,
'Lapis de Escrever', 1.99,
'Sketch Book', 9.50,
'Folhas de ofício', 10.00,
'Lapis de Cor - Fabber Castell', 29.99,
'Marcadores Coloridos', 34.50,
'Tintas Aquarela', 29.99)
num = 0
print (f'{"=="*20}')
print (f'{"LOJA DOS DESENHISTAS":^40}')
print (f'{"=="*20}')
for x in range (0, 7):
    num += 1
    print (f'{loja[num]:.<30}|    ' , end = '')
    print (f'{loja[num+1]:>.2f}')
    num += 1
print (f'{"=="*20}')