def player(j='<desconhecido>', g=0):
    if j == '':
        j = '<desconhecido>'
    print(f'O jogador {j} fez {g} gols no campeonato.')



JOGADOR_ = str(input('Digite o nome do jogador: '))
GOLS_ = str(input(f'Digite a quantidade de gols que {JOGADOR_} fez no campeonato: '))

if GOLS_.isnumeric():
    GOLS_ = int(GOLS_)
else:
    GOLS_ = int(0)

player(JOGADOR_, GOLS_)
