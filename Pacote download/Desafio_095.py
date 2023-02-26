#            INÍCIO
TIME = []
JOGADOR_DICT = {}
GOLS_JOGADOR = []
GOLS_TOTAIS = 0

#            INFORMAÇÕES.
while True:
    JOGADOR_DICT['NOME'] = str (input ('Digite seu nome: ')).title()
    JOGADOR_DICT['PARTIDAS'] = int (input ('Quantas partidas jogadas: '))
        
    for p in range(0, JOGADOR_DICT['PARTIDAS']):
        GOLS_JOGADOR.append(int (input (f'Quantos gols feitos na {p+1}° partida? ')))
        GOLS_TOTAIS += GOLS_JOGADOR[p]
        
    JOGADOR_DICT['GOLS'] = GOLS_JOGADOR[:]
    GOLS_JOGADOR.clear()
    JOGADOR_DICT['TOTAL'] = GOLS_TOTAIS
    GOLS_TOTAIS -= GOLS_TOTAIS
    TIME.append(JOGADOR_DICT.copy())
    
    print ('=' * 30)
    RESP = str (input ('Digite se quer continuar? [S/N] ')).upper()[0]
    print ('=' * 30)
    if RESP not in 'SN':
        while RESP not in 'SN':
            RESP = str (input ('Valor invalido. Deseja continuar? [S/N] ')).upper()[0]
            print ('=' * 30)
    if RESP == 'N':
        break

#            TABELA DO TIME DE FUTEBOL.
print (f'{"------------------------":^60}')
print (f'{"|    TABELA DO TIME    |":^60}')

print ('-' * 64)
print (f'{"NUM":>3}|', end = ' ')
for i in JOGADOR_DICT.keys():
    print (f'{i:^13}|', end = ' ')
print ()

print ('-' * 64)
for k, v in enumerate (TIME):
    print (f'No{k+1}|', end = ' ')
    for d in v.values():
        print (f'{str(d):^13}|', end = ' ')
    print ()
print ('-' * 64)
print (' ')
   
#        INFORMAÇÕES QUE O USUÁRIO DESEJA 
while True:
    NUM = int (input ('Deseja as informações de qual jogador? [999 finaliza] '))
    if NUM > len(TIME):
        if NUM != 999:
            while NUM > len(TIME):
                NUM = int (input ('Jogador invalido... [999 finaliza] '))
                if NUM == 999:
                    break
    
    print ('=' * 55)
    if NUM == 999:
        break    
    NUM -= 1    
    
    
    print (f'O jogador {TIME[NUM]["NOME"]} jogou {TIME[NUM]["PARTIDAS"]} partidas.')
    for p in range(0, TIME[NUM]["PARTIDAS"]):
        print (f'      •→ Na {p+1}° partida fez {TIME[NUM]["GOLS"][p]} gols')
    print (f'Ao total, o jogador fez {TIME[NUM]["TOTAL"]} gols')
    print ('=' * 55)

print ('FINALIZADO, OBRIGADO POR USAR')