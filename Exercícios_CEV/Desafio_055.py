maior = 0
menor = 0

for p in range (1, 6):
    peso = float(input (f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
             maior = peso
        if peso <= menor:
             menor = peso

print (f'\n{maior} é o maior peso registrado.\n{menor} é o menor peso registrado.')