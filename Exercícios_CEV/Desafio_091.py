from random import randrange
from time import sleep
from operator import itemgetter

PLAYERS_PTS = {'jogador 1': randrange(1, 6),
'jogador 2': randrange(1, 6),
'jogador 3': randrange(1, 6),
'jogador 4': randrange(1, 6)}

ORDEM_RANK = {}
ORDEM_RANK = sorted(PLAYERS_PTS.items(), key = itemgetter(1))

for J, P in PLAYERS_PTS.items():
    print (f'{J} tirou: {P} pontos')
    sleep(0.5)

print ('=' * 30)
print (f'{"RANKING:":^30}')

for I, N in enumerate(ORDEM_RANK):
    print (f'{I + 1}° lugar foi {N[0]} que tirou: {N[1]}')
    sleep(0.5)