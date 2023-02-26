from datetime import date

idade = int (input ('Digite seu ano de nascimento: '))
calc = date.today().year - idade

if calc == 18:
    print ('Já é hora de se alistar.')
    
elif calc <= 18:
    print (f'Você irá se alistar em {18 - calc} anos.')

elif calc >= 18:
    print (f'Você passou {calc - 18} anos do seu alistamento')