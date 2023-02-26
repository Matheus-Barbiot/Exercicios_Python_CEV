print ('-='*33)
print ('TEMOS PROMOÇÃO DE R$0,45 PARA CADA KM DE VIAJEMS MAIORES QUE 200KM!')
print ('=-'*33)

n = float (input ('Quantos km serão rodados? '))

if n >= 200:
    print (f'Com a promoção, sua passagem custará R${0.45 * n}')
else:
    print (f'Sua passagem custará R${0.50 * n}')