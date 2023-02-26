from datetime import date

ano = int (input ('Digite seu ano de nascimento: '))
calc = date.today().year - ano

if calc <= 9:
    print ('Mirin.')
elif calc <= 14:
    print ('Infantil.')
elif calc <=  19:
    print ('Junior.')
elif calc == 20:
    print ('Senior.')
elif calc >= 20:
    print ('Master')
