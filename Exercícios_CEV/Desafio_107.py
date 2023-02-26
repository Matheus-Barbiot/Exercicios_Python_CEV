from UtilidadesCEV import moeda

#       INFORMAÇÕES.
NUM_ = float(input('Digite um número: R$'))
print('=' * 45)

#       PORCENTAGENS.
INCREASE_ = int(input('Digite a porcentagem que deseja aumentar: '))
DESCREASE_ = int(input('Digite a porcentagem que deseja diminuir: '))
print('=' * 45)

#       RETORNO.
print(f'Aumentando {INCREASE_}%:    {moeda.aumentar(NUM_, INCREASE_)}')
print(f'Diminuindo {DESCREASE_}%:   {moeda.diminuir(NUM_,DESCREASE_)}')
print(f'O dobro é:  {moeda.dobro(NUM_)}')
print(f'A metade é:     {moeda.metade(NUM_)}')
