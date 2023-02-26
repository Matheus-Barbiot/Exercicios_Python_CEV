countF = 0
countT = 0

for a in range (0, 7):
    idade = int (input ('Digite a sua idade: '))
    idade = 2022-idade
    if idade >= 18:
        countT = countT + 1
    else:
        countF = countF + 1

print (' ')
print (f'{countF} pessoas são menores de idade. \n{countT} pessoas são maiores de idade.')