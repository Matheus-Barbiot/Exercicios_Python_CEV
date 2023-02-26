#            INÍCIO
from datetime import datetime
DADOS_PESSOA = {}

#            INFORMAÇÕES E INDEXAGEM
DADOS_PESSOA['nome'] = str (input ('Digite seu nome: '))
ANO_NACIMENTO = int (input ('Digite seu ano de nascimento: '))
DADOS_PESSOA['idade'] = datetime.now().year - ANO_NACIMENTO
DADOS_PESSOA['ctps'] = int (input ('Digite sua carteira de trabalho: [0 = não tem] '))

#            INFO CARTEIRA
if DADOS_PESSOA['ctps'] != 0:
    DADOS_PESSOA['contratação'] = int (input ('Digite seu ano de contratação: '))
    DADOS_PESSOA['salário'] = int (input ('Digite seu salário: '))
    DADOS_PESSOA['aposentadoria'] = (DADOS_PESSOA['contratação'] - ANO_NACIMENTO) + 32

#            FINALIZANDO    
print ('=' * 30)
for k, d in DADOS_PESSOA.items():
    print (f'O objeto {k} recebe: {d}')