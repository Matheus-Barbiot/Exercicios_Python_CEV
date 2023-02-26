#            INÍCIO
JOGADOR_DICT = {}
GOLS_JOGADOR = []
GOLS_TOTAIS = 0

#            INFORMAÇÕES.
JOGADOR_DICT['NOME'] = str (input ('Digite seu nome: ')).title()
JOGADOR_DICT['PARTIDAS'] = int (input ('Quantas partidas jogadas: '))
print ('=' * 35)

for p in range(0, JOGADOR_DICT['PARTIDAS']):
    GOLS_JOGADOR.append(int (input (f'Quantos gols feitos na {p+1}° partida? ')))
    GOLS_TOTAIS += GOLS_JOGADOR[p]
        
JOGADOR_DICT['GOLS'] = GOLS_JOGADOR[:]
JOGADOR_DICT['TOTAL'] = GOLS_TOTAIS

print ('=' * 35)
print (f'O jogador {JOGADOR_DICT["NOME"]} jogou {JOGADOR_DICT["PARTIDAS"]} partidas:')
for p in range( 0, JOGADOR_DICT["PARTIDAS"]):
    print (f'      •→ {p+1}° partida: {GOLS_JOGADOR[p]} gols')
print (f'No total, o jogador fez  {JOGADOR_DICT["TOTAL"]} gols.')