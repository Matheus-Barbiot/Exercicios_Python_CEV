from UtilidadesCEV import moeda

#       INFORMAÇÕES.
NUM_ = float(input('Digite um número: R$'))
print('=' * 45)

#       PORCENTAGENS.
INCREASE_ = int(input('Digite a porcentagem que deseja aumentar: '))
DESCREASE_ = int(input('Digite a porcentagem que deseja diminuir: '))
print('=' * 45)

#       RETORNO.
print(f'Aumentando {INCREASE_}%:    {moeda.moeda(moeda.aumentar(NUM_, INCREASE_)):^50}')
print(f'Diminuindo {DESCREASE_}%:   {moeda.moeda(moeda.diminuir(NUM_,DESCREASE_)):^50}')
print(f'O dobro é:  {moeda.moeda(moeda.dobro(NUM_)):^50}')
print(f'A metade é:   {moeda.moeda(moeda.metade(NUM_)):^50}')
