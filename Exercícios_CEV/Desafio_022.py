nome = input (str ('Digite seu nome: ')).strip()
print ('Analizando seu nome...')

print (f'Seu nome com letras maiúsculas fica "{nome.upper()}" ')
print (f'Seu nome com letras minúscula fica "{nome.lower()}" ')
print (f'Seu nome tem ao todo é {len(nome) - nome.count(" ")}')
nome = nome.split()

print (f'Seu primeiro nome tem {len (nome [0])} letras')