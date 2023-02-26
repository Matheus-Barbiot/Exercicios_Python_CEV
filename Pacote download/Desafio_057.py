sexo = str (input ('Digite o seu sexo: [F/M] ')).upper()[0]
while sexo not in 'MF':
    sexo = str (input ('Valor incorreto, por favor dogite seu sexo: ')).upper()[0]
print ('Sexo registrado.')