from pessoas import lin
from pessoas import addnome
from pessoas import addidade
from time import sleep

#           CORES ESTÉTICAS
RED_ = '\033[0;31m'
BLUE_ = '\033[0;34m'
CIAN_ = '\033[0;36m'
FIM_ = '\033[m'

#           MENU DO PROGRAMA
while True:
    lin('=', n=40)
    print(f'{"MENU DE CADASTROS":^40}')
    lin('=', n=40)

    print(f'''{BLUE_}    1 - Ver Pessoas Cadastradas:
    2 - Cadastrar Uma Pessoa:
    3 - Finalizar Programa:{FIM_}''')

    while True:
        try:
            lin(n=40)
            OP_ = int(input('Digite Sua Escolha: '))
            if OP_ > 3:
                print(f'{RED_}ERRO! Digite um número VALIDO!{FIM_}')
                continue
            else:
                break

        except ValueError:
            print(f'{RED_}ERRO! Digite um número VALIDO!{FIM_}')
    lin(n=40)
    sleep(2)


#           ESCOLHA NUMERO 1
    if OP_ == 1:
        # ABRINDO ARQUIVOS

        PESSOAS_N = open('Pessoas_nome.txt', 'r')
        LISTA_N = PESSOAS_N.readlines()
        LISTA_N = [x.rstrip('\n') for x in LISTA_N]

        PESSOAS_I = open('Pessoas_idade.txt', 'r')
        LISTA_I = PESSOAS_I.readlines()
        LISTA_I = [x.rstrip('\n') for x in LISTA_I]

        # MOSTRANDO LISTA DE PESSOAS
        lin('=', n=40)
        print(f'{"PESSOAS CADASTRADAS":^40}')
        lin('=', n=40)

        print(RED_,end='')
        if len(LISTA_N) == 0:
            print('Nenhuma pessoa cadastrada ainda!')

        else:
            print(CIAN_, end='')
            for n in range(0, len(LISTA_N)):
                print(f'{n+1} - {LISTA_N[n]}:             \t{LISTA_I[n]}')
        print(FIM_,end='')
        sleep(2)
        PESSOAS_N.close()
        PESSOAS_I.close()

#           ESCOLHA NUMERO 2
    if OP_ == 2:
        lin('=', n=40)
        print(f'{"CADASTRO DE PESSOAS":^40}')
        lin('=', n=40)

        while True:
            NOME_ = str(input('Digite o nome: ')).strip()
            if NOME_ == '' or NOME_.isnumeric():
                print(f'{RED_}ERRO! Digite um nome existente!{FIM_}')
                continue
            else:
                break

        while True:
            IDADE_ = str(input('Digite a idade: ')).strip()
            if IDADE_.isalpha():
                print(f'{RED_}ERRO! Digite uma idade REAL!{FIM_}')
                continue
            else:
                break

        addnome(NOME_)
        addidade(IDADE_)

#           ESCOLHA NUMERO 3
    if OP_ == 3:
        break


print('PROGRAMA FINALIZADO, OBRIGADO POR USAR!')
