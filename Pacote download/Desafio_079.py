lista = []

p = 'sim'
while p != 'não':
    valor = int (input ('Digite um valor: '))
    true = valor in lista
    if true == True:
        print ('valor invalido')
    elif true == False:
        print ('Valor aceito')
        lista.append(valor)
    p = str (input ('deseja continuar? '))
lista.sort()
print (lista)
    