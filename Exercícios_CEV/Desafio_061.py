p1 = int (input ('Digite o primeiro termo da PA: '))
r = int (input ('Digite a razão da PA: '))
count = 0
print (f'{p1},', end = ' ')

while count <= 9:
    count += 1
    print (f'{p1+(r*count)},', end = ' ')
print (' PAUSA ')