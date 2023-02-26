counti = 0
maior = 0
nomeM = ' '
countf = 0

#repetição

for p in range (1, 5):
    print (f'''
{"_ "*4}INFORMAÇÕES DA {p}ª PESSOA {"_ "*4} 
   ''')
    nome = str (input ('Nome: '))
    idade = int (input ('Idade: '))
    genero = str (input ('Genero [M/F]: '))
    
    counti = counti + idade
    
    if idade <= 20 and genero == 'f':
        countf = countf + 1
        
    if p == 1 and genero == 'm':
        maior = idade
        nomeM = nome
    else:
        if idade >= maior and genero == 'm':
            maior = idade
            nomeM = nome

#Separador

print (' ')
print ('=-'*25)
print (' ')

#final

print (f'A média de idade é {counti/4}')
print (f'O homem mais velho tem {maior} e se chama {nomeM}.')
print (f'{countf} mulheres são menores de 20 anos')