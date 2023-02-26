from time import sleep

#Perguntas
valor = float (input ('Qual o valor da casa? R$'))
salario = float (input ('Qual o seu salário? R$'))
anos = int (input ('Em quantos anos você quer pagar? '))

#calculos
calc = valor / anos / 12
porc = salario * 30 / 100

#ano ou anos
if anos == 1:
    an = 'ano'
else:
    an = 'anos'
    
#Cores
vermelho = '\033[31m'
verde = '\033[32m'
final = '\033[m'
 
#Resposta
print ('RECEBENDO RESULTADO. . .')
sleep (2)

print (' ')
print (f'Uma casa de R${valor:.2f}, sendo paga em {anos} {an}, a prestação seria dê: \nR$ {calc:.2f}.')
print (' ')
sleep (1)

if calc >= porc:
    print (f'{vermelho}EMPRESTIMO NEGADO!{final}')

else:
    print (f'{verde}EMPRESTIMO CONCEDIDO!{final}')