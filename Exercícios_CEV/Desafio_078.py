valores = []
maior = 0
menor = 0
for x in range(0,5):
    num = int (input ('Digite um valor: '))
    valores.append(num)
    if x == 1:
        maior = num
        menor = num
    else:
        if num >= maior:
            maior = num
        if num <= menor:
            menor = num

print (f'Os números digitados foram: {valores}')
print (f'O maior número foi {maior} e está na posição {valores.index(maior)+1}.')
print (f'O menor número foi {menor} e está na posição {valores.index(menor)+1}.')