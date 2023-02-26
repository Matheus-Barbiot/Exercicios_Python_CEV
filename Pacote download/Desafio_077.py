palavras = ('Jojo', 'Jonathan', 'Alucard', 'desenho',
'programador', 'curso', 'futuro', 'academia', 'anime', 'calistenia',
'mangá', 'baki', 'artes marciais', 'gamedev', 'inglês')
for p in palavras:
    print (f'\nNa palavra {p.upper()} temos: ', end = '')
    for letra in p:
        if letra in 'aeiou':
            print (letra, end=' ')
    