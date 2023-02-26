#            INICIO.
from random import randrange
from time import sleep

JOGOS = []
PALPITES = []
QUANTIDADE_JOGOS = int (input ('Quantos jogos você quer palpitar? '))

#        GERAÇÃO, ANALIZE E COLOCAÇÃO DO NÚMERO.
for C in range (0 , QUANTIDADE_JOGOS):
    for P in range (0, 6):
        while len(PALPITES) < 6:
            NÚMERO = randrange(0, 60)
            if P == 0:
                PALPITES.append(NÚMERO)
            else:
                while True:
                    if NÚMERO not in PALPITES:
                        PALPITES.append(NÚMERO)
                    else:
                        break

#            FINALIZAÇÃO.
    PALPITES.sort()
    JOGOS.append(PALPITES[:])
    PALPITES.clear()
    print (f'{C+1}ª JOGO: {JOGOS[C]}')
    sleep(0.5)
                