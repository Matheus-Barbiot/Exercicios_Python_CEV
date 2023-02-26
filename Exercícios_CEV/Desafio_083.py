exp = str (input ('Digite uma expressão: '))
p1 = exp.count('(')
p2 = exp.count(')')

if p1 == p2:
    print ('Está certo')
else:  
    print ('Está errado')