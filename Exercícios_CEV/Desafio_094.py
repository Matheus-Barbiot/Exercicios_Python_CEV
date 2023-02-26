#            INÍCIO.
DADOS_PESSOA = {}
PESSOAS_LISTA = []
MEDIA_IDADE = 0
P_ACIMA_MEDIA = []
M_CADASTRADAS = []

#            ADD INFORMAÇÕES.
while True:
    DADOS_PESSOA['nome'] = str (input ('Nome: ')).title()
    DADOS_PESSOA['sexo'] = str (input ('Sexo: [F/M] ')).upper()[0]
    while DADOS_PESSOA['sexo'] not in 'MF':
        DADOS_PESSOA['sexo'] = str (input ('Sexo invalido: [F/M] ')).upper()[0]
    
    DADOS_PESSOA['idade'] = int (input ('Idade: '))
    
    PESSOAS_LISTA.append(DADOS_PESSOA.copy())
    MEDIA_IDADE += DADOS_PESSOA['idade']
    if DADOS_PESSOA['sexo'] == 'F':
        M_CADASTRADAS.append(DADOS_PESSOA['nome'])
      
    #    CONTINUAR.
    print ('=' * 30)
    CONTINUE = str (input ('Deseja continuar? [S/N]')).upper()[0]
    while CONTINUE not in 'SN':
        CONTINUE = str (input ('Valor invalido, deseja continuar? [S/N] ')).upper()[0]
    print ('=' * 30)
    
    if CONTINUE == 'N':
        break

#            MEDIA DE IDADE.
MEDIA_IDADE = MEDIA_IDADE / len(PESSOAS_LISTA)

#            FINALIZANDO (1/0).
print (f'A) Foram {len(PESSOAS_LISTA)} cadastradas ao todo')

print (f'B) A média de idade foi {MEDIA_IDADE:2.2f}')

print (f'C) As mulheres cadastradas foram: ', end = ' ')

for m in range (0, len(M_CADASTRADAS)):
    print (f'{M_CADASTRADAS[m].title()}, ', end = ' ')
print ( )

print ('D) Pessoas com idade acima da media:')
for p in PESSOAS_LISTA:
    if p['idade'] >= MEDIA_IDADE:
        for k, v in p.items():
            print (f'    • {k} = {v}; ', end = ' ')
print ( )
        