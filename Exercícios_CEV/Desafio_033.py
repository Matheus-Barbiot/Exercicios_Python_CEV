a = int (input ('Primeiro número: '))
b = int (input ('Segundo número: '))
c = int (input ('Terceiro número: '))
print (' ')

#Calculando o menor:
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print (f'O menor número é {menor}.')

#Calculando o maior:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print (f'O maior número é {maior}.')
