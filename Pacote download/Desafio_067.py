n = 0

while n >= 0:
    print ('='*50)
    n = int (input ('Digite um número: '))
    print ('='*50)
        
    if n <= 0:
        break

    for num in range (1, 11):
        print (f'{n} x {num} = {n*num}')

print ('Programa finalizando, obrigado por usar.')