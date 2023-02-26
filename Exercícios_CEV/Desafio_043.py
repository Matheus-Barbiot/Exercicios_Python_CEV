peso = float (input ('Digite seu peso: '))
altura = float (input ('Digite sua altura: '))
calc = peso / altura ** 2
print (f'Seu IMC é {calc:.1f}: ')

if calc <= 18.5:
    print ('Você está abaixo do peso. . .')
elif calc <= 25:
    print ('Parabéns, você tem o peso ideal!')
elif calc <= 30:
    print ('Você é sobre peso.')
elif calc <= 40:
    print ('Você é obeso.')
elif calc >= 40:
    print ('você tem obesisdade mórbida.')