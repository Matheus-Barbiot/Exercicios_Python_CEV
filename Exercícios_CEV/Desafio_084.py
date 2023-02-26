PESSOAS = []
DADOS = []
PESO_PESADO = PESO_LEVE = 0

while True:
    DADOS.append(str (input ('Digite seu Nome: ')))
    DADOS.append(int (input ('Digite seu peso: ')))
    print ('='*50)
    if len(PESSOAS) == 0:
        PESO_PESADO = PESO_LEVE = DADOS[1:]
    else:
        if DADOS[1:] > PESO_PESADO:
            PESO_PESADO = DADOS[1:]
        if DADOS[1:] < PESO_LEVE:
            PESO_LEVE = DADOS[1:]
            
    PESSOAS.append(DADOS[:])
    DADOS.clear()
    
    
    CONTINUAR = str (input ('Deseja continuar: '))
    if CONTINUAR == 'não':
        break
    
    print ('='*50)
print (f'Número de pessoas cadastradas: {len(PESSOAS)}.')
print (f'O peso mais pesado foi {PESO_PESADO[0]}.')
print (f'O peso Mais leve foi {PESO_LEVE[0]}.')