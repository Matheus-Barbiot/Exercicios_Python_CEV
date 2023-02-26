tabela = ('PAL', 'INT', 'FLU', 'COR', 'FLA', 'CAP', 'ATL', 'FOR', 'SAO', 'AMG', 'BOT', 'SAN', 'GOI', 'RBB', 'CBA', 'CUI', 'CEA', 'AGO', 'AVA', 'JUV')

print ('÷='*25)
print (f'''Lista de times do Brasileirão:
{tabela}''')

print ('÷='*25)
print (f'''Os 5 primeiros colocados são:
{tabela[0:5]}''')

print ('÷='*25)
print (f'''A lista em ordem alfabética: 
{sorted(tabela)}''')

print ('÷='*25)
print (f'''O Inter está como:
{tabela.index("INT")+1}° Colocado''')