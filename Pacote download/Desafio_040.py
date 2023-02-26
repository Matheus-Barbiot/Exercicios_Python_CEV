nota1 = float (input ('Primeira nota: '))
nota2 = float (input ('Segunda nota: '))
calc = (nota1 + nota2) / 2

if calc <= 5:
    print ('REPROVADO!')
elif calc >= 7:
    print ('APROVADO!')
else:
    print ('Recuperação...')