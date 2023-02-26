escolha = 'sim'
Nu1 = 0
Nu2 = 0
Nu3 = 0

while True:
    print (f'''
{"÷="*25}
                CADASTRE UMA PESSOA:
{"÷="*25}
''')

# PEDINDO INFORMAÇÕES
    idade = int (input ('Digite sua idade: '))
    sexo = str (input ('Digite seu sexo: '))

    if idade >= 17:
        Nu1 += 1
    if sexo == 'm':
        Nu2 += 1
    if sexo == 'f' and idade <= 19:
        Nu3 += 1


# ESCOLHA    
    escolha = str (input (f'''
{"-"*50}
Você quer continuar? '''))
    print ('-'*50)
    
    if escolha == 'não':
        break
    
print (f'{Nu1} Pessoas não têm mais que 18 anos')
print (f'{Nu2} Homens foram cadastrados.')
print (f'{Nu3} Mulheres são menores de 20 anos')