valor = float (input ('Digite o valor do produto: R$'))
print ('''
FORMAS DE PAGAMENTO:
1: Á vista dinheiro/cheque: 10% de desconto.
2: Á vista cartão: 5% de desconto.
3: Em até 2x no cartão: preço normal.
4: 3x ou mais no cartão: 20% de juros.
''')
op = int (input ('Sua escolha: '))

if op == 1:
    calc = valor * 10 / 100
    print (f'Seu produto custará R${valor-calc:.2f} á vista.')

elif op == 2:
    calc = valor * 5 / 100
    print (f'Seu produto custará R${valor - calc:.2f} á vista.')

elif op == 3:
    print (f'Seu produto custará R${valor / 2:.2f} ')

elif op == 4:
    calc = valor * 20 / 100
    print (f'Seu produto custará R${valor / 2 + calc:.2f} ')
