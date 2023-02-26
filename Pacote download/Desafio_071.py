count50 = 0
count20 = 0
count10 = 0
count01 = 0

print (f'''{"=÷"*25}
                BANCO DO HETERO
{"=÷"*25}''')

saque = int (input ('Quanto você quer sacar? '))

while True:
    C50 = saque / 50
    count50 += 1
    
    if C50 % 0:
        break

print (f'Você precisa de {count50} cedula de 50.')