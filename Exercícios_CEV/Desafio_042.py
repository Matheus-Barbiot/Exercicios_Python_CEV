a = float (input ('Digite a primeira reta: '))
b = float (input ('Digite a segunda reta: '))
c = float (input ('Digite a terceira reta: '))

if a + b > c:
    print ('É possível criar um triângulo!')
    if a == b and b == c:
        print ('Este triângulo é EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print ('Este triângulo é ISÓSCELES.')
    else:
        print ('Este triângulo é ESCALENO.')
    
else:
    print ('Não é possível criar um triângulo')