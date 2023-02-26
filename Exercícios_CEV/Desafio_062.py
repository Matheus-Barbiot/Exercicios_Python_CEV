p1 = int (input ('Digite o primeiro termo da PA: '))
r = int (input ('Digite a razão da PA: '))
count = 0
termo = p1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while count <= total:
        termo += r
        count += 1
        print (f'{termo},', end = ' ')
    print (' PAUSA ')
    mais = int (input ('Quantos termos você quer mostrar a mais? '))
print (f'Progressão finalizada com {total} termos mostrados.')