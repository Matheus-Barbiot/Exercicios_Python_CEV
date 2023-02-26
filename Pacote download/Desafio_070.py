soma = Nu1 = Nu2 = count = 0
Nu3 = ' '

print (f'''{"÷="*25}
               AMAZON DO PARAGUAI:
{"÷="*25}
''')

#            REPETIÇÃO

while True:
    
#            INFORMAÇÕES 

    nome = str (input ('Nome do produto: '))
    preco = int (input ('Preço do produto: R$'))

#            SOMA

    soma += preco
    count += 1

    if preco >= 999:
        Nu1 += 1    

    if count == 1 or preco <= Nu2:
        Nu2 = preco
        Nu3 = nome

#            ESCOLHA

    escolha = str (input (f'''{"-"*50}
                Deseja continuar? '''))
    print (f'{"-"*50}')
    
#            FINALIZAR

    if escolha == 'não':
        break
print (f'Você gastou R${soma} nas suas compras.')
print (f'Você conprou {Nu1} produtos com mais de R$1000')
print (f'{Nu3} é o produto mais barato e custa R${Nu2}.')