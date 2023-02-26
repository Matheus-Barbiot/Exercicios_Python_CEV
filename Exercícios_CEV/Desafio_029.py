km = int (input ('Quantos km/h seu carro anda? '))
if km >= 81:
    print (f'MULTADO! você terá que pagar uma multa de R${(km-80)*7},00. . .')
else:
    print (f'Muito bem, dirija com segurança!')