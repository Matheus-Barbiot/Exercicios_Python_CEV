x = (int (input ('Digite o primeiro valor: ')), 
int (input ('Digite o segundo valor: ')),
int (input ('Digite o terceiro valor: ')),
int (input ('Digite o quarto valor: ')))

print ('=÷'*25)
#           ANALISE DE TUPLA.

print (f'O número 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print (f'O número 3 aparece na posição {x.index(3)+1}')
else:
    print ('O valor 3 não foi digitado')
print ('Os numeros pares digitados são: ', end = ' ')
for n in x:
    if n % 2 == 0:
        print (n, end = ' ')