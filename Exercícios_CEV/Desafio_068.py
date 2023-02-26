from random import randrange
count = 0
win = ' '
botnum = randrange(0, 12)

print ('-='*25)
print ('JOGO DO PAR OU IMPAR')
print ('=-'*25)

while win != 'lose':
    num = int (input ('Digite um número: '))
    
    print ('='*50)
    escolha = str (input ('Escolha par ou impar? '))
    print (' ')
    
    soma = (num + botnum) % 2
    
# GANHAR
    if soma == 0 and escolha == 'par':
        print (f'VOCÊ VENCEU! Eu escolhi {botnum} e você {num}, deu PAR.')
        count += 1
        print (' ')
        print (f'{"="*10} VAMOS JOGAR NOVAMENTE {"="*10}')
        
    if soma >= 1 and escolha == 'impar':
        print (f'VOCÊ VENCEU! Eu escolhi {botnum} e você {num}, deu IMPAR.')
        count += 1
        print (' ')
        print (f'{"="*10} VAMOS JOGAR NOVAMENTE {"="*10}')
        
# PERDER
    if soma == 0 and escolha == 'impar':
        print (f'VOCÊ PERDEU! você ganhou {count} vezes.')
        win = 'lose'
    
    if soma >= 1 and escolha == 'par':
        print (F'VOCÊ PERDEU! você ganhou {count} vezes.')     
        win = 'lose'