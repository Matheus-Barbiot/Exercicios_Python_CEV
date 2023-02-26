n1 = int (input ('Digite o primeiro termo da PA: '))
r = int (input ('Digite a razão da PA: '))

for pa in range (0, 10):
    calc = n1+(r*pa)
    print (f' {calc},', end=' ')
print (' FINAL')