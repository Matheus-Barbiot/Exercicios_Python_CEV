termos = int (input ('Digite o número de sequência: '))
count = 2
n1 = 0
n2 = 1
n3 = n1 + n2

if termos == 1:
    print (f'{n1} →', end = ' ')
else:
    print (f'{n1} → {n2} →', end = ' ')
    while count != termos:
        count += 1
        print (f'{n3} →', end = ' ')
        n1 = n2
        n2 = n3
        n3 = n1+ n2
print ('FINAL ')