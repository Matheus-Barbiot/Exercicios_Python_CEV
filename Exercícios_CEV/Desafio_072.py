números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Deis', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Desoito', 'Dezenove', 'Vinte')
num = int (input ('Digite um número: '))

while True:
    if num <= 21 and num >= 0:
        break
    num = int (input ('Número inválido digite novamente: '))

print (f'Você digitou o número {números[num]}.')