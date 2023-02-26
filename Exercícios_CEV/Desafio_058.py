from random import randrange 

counter = 0

print ('Eu pensei em um número de 0 a 10.')
n = int (randrange (0, 11))
palpite = int (input ('Qual o seu palpite? '))

while palpite != n:
    if palpite >= n:
        palpite = int (input ('Menos... tente novamente: '))
    elif palpite <= n:
        palpite = int (input ('Mais... tente novamente: '))
    counter = counter + 1

print (f'Numero certo!! você precisou de {counter} tentativas para ganhar.')