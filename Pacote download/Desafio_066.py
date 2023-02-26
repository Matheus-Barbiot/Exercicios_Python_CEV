n = 0 
s = n
c = 0

while n != 999:
    n = int (input ('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print (f'Você digitou {c} números e a soma dos números digitados é {s}')
    